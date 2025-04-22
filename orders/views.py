from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
from .pagination import OrderListPagination


class OrderListCreateAPIView(APIView):
    def get(self, request):
        orders = Order.objects.prefetch_related('items').all()
        paginator = OrderListPagination()
        results = paginator.paginate_queryset(orders, request, view=self)
        serializer = OrderSerializer(results, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return None

    def put(self, request, pk):
        order = self.get_object(pk)
        if not order:
            return Response({'error': 'Order is not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = self.get_object(pk)
        if not order:
            return Response({'errors': 'Order is not found'}, status=status.HTTP_404_NOT_FOUND)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


