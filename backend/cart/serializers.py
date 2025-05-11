from rest_framework import serializers

from .models import Cart, CartItem

from products.serializers import ProductGETSerializer
from products.models import Product


class CartSerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField(
        method_name='get_products_count')

    class Meta:
        model = Cart
        fields = ('id', 'products_count')

    def get_products_count(self, obj):
        return CartItem.objects.filter(cart=obj).count()


class CartGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartRETRIEVESerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField(method_name='get_products')

    class Meta:
        model = Cart
        fields = ('id', 'products', 'user', 'status', 'formed_at',
                  'created_at', 'finished_at', 'moderator', )

    def get_products(self, obj):
        products_ids = CartItem.objects.filter(
            cart=obj).values_list('product', flat=True)
        products = Product.objects.filter(id__in=products_ids)
        serializer = ProductGETSerializer(instance=products, many=True)
        return serializer.data


class CartItemPUTSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('quantity', )
