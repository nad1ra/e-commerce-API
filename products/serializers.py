from rest_framework import serializers
from categories.serializers import CategorySerializer
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category']