from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .paginations import CommonListPagination 


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    pagination_class = CommonListPagination

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