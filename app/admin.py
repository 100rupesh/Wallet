from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Expense)
# admin.site.register(Profile)


class UserAdmin(admin.ModelAdmin):
    
    list_display=("id","user", "balance", "is_active")

admin.site.register(Profile,UserAdmin)