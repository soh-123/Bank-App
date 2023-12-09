from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transaction
import csv

def login(request):
    if request.method == 'POST':
        user_email = request.POST.get('user_email')
        try:
            user = Transaction.objects.get(email=user_email)
        except Transaction.DoesNotExist:
            return render(request, 'login.html', {'error_message': 'Invalid email'})
        
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        return redirect('user_home', start_date=start_date, end_date=end_date)

    return render(request, 'login.html')

def user_home(request):
    transactions = Transaction.objects.order_by("date_of_transaction")
    return render(request, "userprofile/home.html", {'transactions': transactions})

def download_bank_statement(request):
    transactions = Transaction.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="bank_statement.csv"'

    csv_writer = csv.writer(response)
    csv_writer.writerow(['User Email', 'Date of Transaction', 'Amount'])

    for transaction in transactions:
        csv_writer.writerow([transaction.user_email, transaction.date_of_transaction, transaction.amount])

    return response


