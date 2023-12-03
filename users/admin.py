from django.contrib import admin

from .models import *

class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'birthdate']
    list_filter = ['user', 'gender']

admin.site.register(Account, AccountAdmin)