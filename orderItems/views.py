from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OrderItem
from .serializers import OrderItemSerializer


class OrderItemListAPIView(APIView):
    def get(self, request):
        orders = OrderItem.objects.prefetch_related('order_items').all()
        serializer = OrderItemSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderItemDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return OrderItem.objects.get(pk=pk)
        except OrderItem.DoesNotExist:
            return None

    def put(self, request, pk):
        orderItem = self.get_object(pk)
        if not orderItem:
            return Response({'error': 'OrderItem is not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = OrderItemSerializer(orderItem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        orderItem = self.get_object(pk)
        if not orderItem:
            return Response({'errors': 'OrderItem is not found'}, status=status.HTTP_404_NOT_FOUND)
        orderItem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



