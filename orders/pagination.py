from rest_framework.pagination import PageNumberPagination

class OrderListPagination(PageNumberPagination):
    page_size = 12