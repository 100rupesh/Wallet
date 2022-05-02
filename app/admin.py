from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
# Register your models here.

# admin.site.register(Profile)


class ProfileAdmin(admin.ModelAdmin):
    list_display=("id","user", "balance", "is_active")

admin.site.register(Profile,ProfileAdmin)



class ExpenseAdmin(admin.ModelAdmin):
    list_display=("id","user", "amount", "exp_type")

admin.site.register(Expense,ExpenseAdmin)