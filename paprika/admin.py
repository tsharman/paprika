
from django.contrib import admin
from paprika.models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'cust_name', 'cust_email', 'current_stage')

admin.site.register(Order, OrderAdmin) 
