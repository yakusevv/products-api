from django.urls import path
from rest_framework import routers

from .views import ProductViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='product-list')
router.register('categories', CategoryViewSet, basename='category-list')

urlpatterns = router.urls