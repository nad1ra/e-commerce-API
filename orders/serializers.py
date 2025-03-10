from rest_framework import serializers
from orderItems.serializers import OrderItemSerializer
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'customer_email', 'customer_phone', 'total_price', 'status', 'created_at', 'order_items']

