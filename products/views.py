from django.shortcuts import render
from rest_framework.generics import ListAPIView
from products.models import ProductsCategory, Makers, Products

from products.serializers import (
    MakerSerializer,
    ProductSerializer,
    ProductsCategorySerializer,
)


class ProductsCategoryListView(ListAPIView):
    serializer_class = ProductsCategorySerializer
    queryset = ProductsCategory.objects.all()
    depth = 1


class MakerListView(ListAPIView):
    serializer_class = MakerSerializer
    queryset = Makers.objects.all()


class ProductsListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()
