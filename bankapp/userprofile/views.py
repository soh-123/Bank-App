from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transaction
from django.core.mail import EmailMessage
import csv
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



def filter_transactions(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')

        # Query the database to filter transactions based on email and date range
        transactions = Transaction.objects.filter(
            user_email=email,
            date_of_transaction__range=[start_date, end_date]
        ).order_by('date_of_transaction')

        # Convert transactions to a list of dictionaries
        transactions_list = [
            {
                'user_email': transaction.user_email,
                'date_of_transaction': transaction.date_of_transaction,
                'amount': transaction.amount,
            }
            for transaction in transactions
        ]

        # Return the filtered transactions as JSON response
        return JsonResponse({'transactions': transactions_list})

    # Handle other HTTP methods or invalid requests
    return JsonResponse({'error': 'Invalid request method'})


def user_home(request):
    transactions = Transaction.objects.order_by("date_of_transaction")
    return render(request, "userprofile/home.html", {'transactions': transactions})


def download_bank_statement(request):
    """
    Download bank statement as a CSV file
    """
    transactions = Transaction.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="bank_statement.csv"'

    csv_writer = csv.writer(response)
    csv_writer.writerow(['User Email', 'Date of Transaction', 'Amount'])

    for transaction in transactions:
        csv_writer.writerow([transaction.user_email, transaction.date_of_transaction, transaction.amount])

    return response

@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        email = EmailMessage(
            'Bank Statement',
            'Please find your bank statement attached.',
            os.environ.get("EMAIL_HOST_USER"), 
            ["sohier.lotfy@hotmail.com"], 
        )
        # Attach the CSV file
        _, csv_data = download_bank_statement(request)
        email.attach('bank_statement.csv', csv_data, 'text/csv')

        # Send the email
        try:
            email.send()
            return JsonResponse({'message': 'Email sent successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
        
    return JsonResponse({'error': 'Invalid request method'})
