from django.contrib import admin
from .models import Order, Pizza, Customer


admin.site.register(Pizza)
admin.site.register(Order)
admin.site.register(Customer)
