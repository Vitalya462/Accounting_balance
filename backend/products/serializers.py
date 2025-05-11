from rest_framework import serializers

from .models import Product


class ProductImageSerializer(serializers.Serializer):
    image = serializers.ImageField(required=True)


class ProductPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description',
                  'price', 'work_format', 'industry', )
        extra_kwargs = {
            'work_format': {'required': False},
            'industry': {'required': False},
        }


class ProductPUTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description',
                  'price', 'work_format', 'industry', )


class ProductGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = rep['image'].replace('http://minio', 'http://localhost')
        return rep
