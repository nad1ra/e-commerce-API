from rest_framework.pagination import PageNumberPagination

class OrderItemListPagination(PageNumberPagination):
    page_size = 12