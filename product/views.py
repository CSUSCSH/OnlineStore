from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from product.models import Category, Product, ProductImage
from product.serializers import CategorySerializer, ProductSerializer, ProductImageSerializer

# User = get_user_model()


class CategoryViewSet(viewsets.ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductImageViewSet(viewsets.ModelViewSet):

    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.all()
