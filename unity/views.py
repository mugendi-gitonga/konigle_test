import calendar
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from datetime import date, datetime


# Create your views here.


def home(request):

    return render (request, 'store.html')


class EmailSignupView(APIView):

    def get(self, request):

        customer_detail = CustomerEmail.objects.all()
        serialized_detail = CustomerEmailSerializer(customer_detail)

        return Response(serialized_detail.data,many=True)


    def post(self, request):

        info = request.data
        serialized_detail = CustomerEmailSerializer(data=request.data)

        if serialized_detail.is_valid():
            serialized_detail.save()
        
            return Response({'message':'new email subscribed successfully'}, status=status.HTTP_200_OK)
        else:
            try:
                customer = CustomerEmail.objects.get(email=info['email'])
                if customer.status is True:
                    customer.status = False
                    customer.save()
                    return Response({'message':'unsubscribed successfully'}, status=status.HTTP_200_OK)
                elif customer.status is False:
                    customer.status = True
                    customer.save()
                    return Response({'message':'subscribed successfully'}, status=status.HTTP_200_OK)

            except:
                return Response({
                    'message':'an error occured',
                    'details':serialized_detail.errors
                    },
                    status=status.HTTP_406_NOT_ACCEPTABLE)


def dashboard(request):
    
    today = date.today()
    
    current_year = today.year
    current_month = today.month
    current_month_name = calendar.month_name[current_month]

    all_emails = CustomerEmail.objects.all().order_by("-creation_date")
    this_month_emails = all_emails.filter(creation_date__month=current_month, creation_date__year=current_year).count()
    unsubscribed_emails = all_emails.filter(status=False).count()

    context = {
        "emails":all_emails,
        "current_month_name":current_month_name,
        "current_year":current_year,
        "this_month_emails":this_month_emails,
        "unsubscribed_emails":unsubscribed_emails
    }

    return render (request, 'dashboard.html', context)

