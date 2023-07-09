from django.contrib import admin
from django.urls import include, path
from .views import MakerListView, ProductsCategoryListView, ProductsListView

app_name = "products"
urlpatterns = [
    path("categories", ProductsCategoryListView.as_view(), name="categories-list"),
    path("makers", MakerListView.as_view(), name="makers-list"),
    path("", ProductsListView.as_view(), name="products-list"),
]
