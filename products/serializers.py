from rest_framework import serializers

from .models import ProductsCategory, Makers, Products


class ProductsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsCategory
        fields = "__all__"
        depth = 1


class MakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Makers
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
        depth = 1
