from django.db import models
from django.contrib.auth.models import User
from sqlalchemy import null
from datetime import datetime
# Create your models here.
TYPE=(
    ("positive","positive"),
    ("negative","negative")

)
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    balance=models.FloatField(blank=True,null=True)
    is_active=models.BooleanField(default=False)
    


class Expense(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    exp_type=models.CharField(max_length=50,choices=TYPE)
    amount=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True, blank=True)
