from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .paginations import CommonListPagination


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    pagination_class = CommonListPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = {"category": ["in"]}
    search_fields = ["name", "description", "category__name"]
    ordering_fields = [
        "name",
        "description",
        "price",
        "quantity",
        "add_dattime",
        "category",
    ]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductSerializer(instance)
        return Response(serializer.data)

    def get_object(self):
        return get_object_or_404(Product, id=self.kwargs.get("pk"))

    def get_queryset(self):
        return Product.objects.all()


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    pagination_class = CommonListPagination

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CategorySerializer(instance)
        return Response(serializer.data)

    def get_object(self):
        return get_object_or_404(Category, id=self.kwargs.get("pk"))

    def get_queryset(self):
        return Category.objects.all()
