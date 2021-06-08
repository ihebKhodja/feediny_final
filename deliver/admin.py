from django.contrib import admin

from django.contrib import admin
from .models import Restaurant, Category, Meal, Order, Cart

admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(Cart)