from django.urls import path, include

from . import views

from rest_framework.routers import SimpleRouter


product_router = SimpleRouter()
product_router.register('', views.ProductViewSet, basename='products')

urlpatterns = [
    path('', include(product_router.urls)),
]
