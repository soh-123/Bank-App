import os
import csv
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings

filter_output = []


def user_home(request):
    error_message = None

    if request.method == 'POST':
        email = request.POST.get('email')
        start_date = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d').date()
        end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d').date()

        with open("static/transactions.csv") as file:
            csvreader = csv.reader(file)
            next(csvreader) 

            for row in csvreader:
                row_email, amount, date_str = row
                date = datetime.strptime(date_str, '%d-%m-%Y').date()
                if email == row_email and start_date <= date <= end_date:
                    global filter_output
                    filter_output.append((date, float(amount)))
        
        if not filter_output:
            error_message = "This email address doesn't exist."
    return render(request, "userprofile/home.html", {'error_message': error_message})


def download_bank_statement(request):
    if filter_output:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="bank_statement.csv"'

        csv_writer = csv.writer(response)
        csv_writer.writerow(['Date of Transaction', 'Amount'])

        for transaction in filter_output:
            csv_writer.writerow(transaction)
        return response
    else:
        return HttpResponse("No data available for download.")


def send_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if 'send_email' in request.POST:
            subject = 'Bank Statement'
            message = 'Please find attached the bank statement CSV file'
            from_email = settings.EMAIL_HOST_USER
            try:
                send_mail(
                    subject, 
                    message, 
                    from_email, 
                    ['sohier.lotfy@hotmail.com'], #change to any email
                    fail_silently=False, 
                    attach_file=os.path.join(settings.STATIC_ROOT, "transaction_report.csv"))
            except Exception as e:
                return JsonResponse({'success': False, 'message': str(e)}) 
    return JsonResponse({'error': 'Invalid request method'})
