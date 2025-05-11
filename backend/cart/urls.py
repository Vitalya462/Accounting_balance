from django.urls import path, include

from . import views

from rest_framework.routers import SimpleRouter


cart_router = SimpleRouter()
cart_router.register('', views.CartViewSet, basename='carts')

cart_item_router = SimpleRouter()
cart_item_router.register(
    'product', views.CartItemViewSet, basename='cart_item')

urlpatterns = [
    path('', include(cart_item_router.urls)),
    path('', include(cart_router.urls))
]
