from __future__ import absolute_import

from celery import shared_task
from datetime import date
from .models import CustomerEmail

@shared_task
def print_new_email_counts():

    today = date.today()
    current_year = today.year
    current_month = today.month

    this_month_emails = CustomerEmail.objects.filter(creation_date__month=current_month, creation_date__year=current_year).count()
    
    print(str(this_month_emails) + ' new emails this month')

    return (str(this_month_emails) + ' new emails this month')


