from rest_framework import serializers
from ecommerce_app.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "image", "quantity"]
