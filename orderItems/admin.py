from django.contrib import admin
from .models import OrderItem

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'price')
    search_fields = ('product', 'price')