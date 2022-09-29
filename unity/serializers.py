
from django.db.models import fields
from rest_framework import serializers
from .models import *


class CustomerEmailSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = CustomerEmail
        fields = '__all__'
