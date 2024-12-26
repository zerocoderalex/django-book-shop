from django.contrib import admin
from .models import Book, User, Order, OrderItem

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(OrderItem)