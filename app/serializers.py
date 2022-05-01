from attr import fields
from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields='__all__'