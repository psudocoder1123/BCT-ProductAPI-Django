from django.shortcuts import render
from rest_framework import generics
from ecommerce_app.serializers import ProductSerializer
from ecommerce_app.models import Product

# Create your views here.


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product
    serializer_class = ProductSerializer
