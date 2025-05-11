from rest_framework import serializers

from .models import ProductIndustry, ProductWorkFormat


class ProductIndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductIndustry
        fields = ('name', )


class ProductWorkFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductWorkFormat
        fields = ('name', )
