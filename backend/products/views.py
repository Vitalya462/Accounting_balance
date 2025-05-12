from cart.models import CartItem, Cart

from products.models import Product
from products.serializers import ProductGETSerializer, ProductPOSTSerializer, ProductImageSerializer, ProductPUTSerializer

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema

from minio_storage.storage import MinioMediaStorage


class ProductViewSet(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    http_method_names = ('get', 'post', 'put', 'delete')

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'GET':
            return ProductGETSerializer(*args, **kwargs)
        elif self.request.method == 'POST':
            return ProductPOSTSerializer(*args, **kwargs)
        elif self.request.method == 'PUT':
            return ProductPUTSerializer(*args, **kwargs)

    @extend_schema(request={
        'multipart/form-data': {
            'type': 'object',
            'properties': {
                'image': {
                    'type': 'string',
                    'format': 'binary'
                }
            }
        }
    })
    @action(methods=['post'], detail=True, url_path='add_image', url_name='add-image')
    def add_image_to_product(self, request, *args, **kwargs):
        product = self.get_object()
        image_serializer = ProductImageSerializer(data=request.data)
        image_serializer.is_valid(raise_exception=True)
        image = image_serializer.validated_data['image']
        product = self.get_object()
        storage = MinioMediaStorage()
        if product.image.name:
            storage.delete(product.image.name)
        product.image = image
        product.save()

        return Response({'detail': 'Image added'})

    @extend_schema(request=None)
    @action(methods=['post', ], detail=True, url_path='add_product_into_draft', url_name='add-product-into-draft')
    def add_product_into_draft(self, request, *args, **kwargs):
        product = self.get_object()
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        CartItem.objects.get_or_create(product=product, cart=cart)
        return Response(data={'product added': product.id})
