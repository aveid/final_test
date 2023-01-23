from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductsAPIView.as_view())
]