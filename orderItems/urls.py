from django.urls import path
from .views import OrderItemListAPIView, OrderItemDetailAPIView

urlpatterns = [
    path('orderItems/', OrderItemListAPIView.as_view(), name='orderItems-list'),
    path('orderItems/<int:pk>/', OrderItemDetailAPIView.as_view(), name='orderItems-detail'),
]