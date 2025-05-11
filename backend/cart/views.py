from .models import Cart, CartItem
from .serializers import CartGETSerializer, CartRETRIEVESerializer, CartSerializer, CartItemPUTSerializer
from .enums import CartStatus

from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.decorators import action, permission_classes
from rest_framework import status
from rest_framework.generics import get_object_or_404

from web_shop.perms import IsModerator

from drf_spectacular.utils import extend_schema


class CartViewSet(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartGETSerializer
    http_method_names = ('get', 'put', 'delete', )

    def list(self, request, *args, **kwargs):
        status = request.query_params.get('status', None)
        queryset = self.get_queryset()
        if status:
            queryset = queryset.filter(status=status)
        filtered_queryset = queryset.exclude(status__in=('D', 'DEL', ))
        date_from = request.query_params.get('from', None)
        date_to = request.query_params.get('to', None)
        if date_from:
            filtered_queryset = filtered_queryset.filter(
                created_at__gte=date_from)
        if date_to:
            filtered_queryset = filtered_queryset.filter(
                created_at__lte=date_to)

        serializer = self.get_serializer(filtered_queryset, many=True)
        return Response(data=serializer.data)

    def retrieve(self, request, *args, **kwargs):
        cart = self.get_object()
        serializer = CartRETRIEVESerializer(instance=cart)
        return Response(serializer.data)

    @extend_schema(request=None, responses={'detail': str})
    @action(methods=['put', ], detail=True, url_name='forming')
    def form_cart(self, request, pk, *args, **kwargs):
        cart = self.get_object()
        user = request.user
        if cart.user == user:
            cart.status = CartStatus.FORMED
            cart.save()
            return Response({'detail': 'Корзина сформирована'})
        return Response({'detail': 'Только создатель корзины может ее сформировать'}, status=status.HTTP_403_FORBIDDEN)

    @extend_schema(request=None, responses={'detail': str})
    @permission_classes((IsModerator, ))
    @action(methods=['put', ], detail=True, url_name='reject')
    def reject_cart(self, request, pk, *args, **kwargs):
        cart = self.get_object()
        user = request.user
        cart.moderator = user
        cart.status = CartStatus.REJECTED
        cart.save()
        return Response({'detail': 'Корзина отклонена'}, status=status.HTTP_200_OK)

    @extend_schema(request=None, responses={'detail': str})
    @permission_classes((IsModerator, ))
    @action(methods=['put', ], detail=True, url_name='complete')
    def complete_cart(self, request, pk, *args, **kwargs):
        cart = self.get_object()
        user = request.user
        cart.moderator == user
        cart.status = CartStatus.COMPLETED
        cart.save()
        return Response({'detail': 'Корзина завершена'}, status=status.HTTP_200_OK)

    @action(methods=['get', ], detail=False, url_path='my_draft_cart', url_name='my-draft-cart')
    def my_draft_cart(self, request, *args, **kwargs):
        user = request.user
        cart = Cart.objects.get(user=user)
        if cart.status != CartStatus.DRAFT:
            return Response({'detail': 'У вас нет черновиков корзины'})
        serializer = CartSerializer(cart)
        return Response(serializer.data)


@extend_schema(tags=['CartItem'])
class CartItemViewSet(DestroyModelMixin, UpdateModelMixin, GenericViewSet):
    http_method_names = ('delete', 'put', )
    queryset = CartItem.objects.all()
    serializer_class = CartItemPUTSerializer

    def get_object(self):
        queryset = self.get_queryset()
        user = self.request.user
        product = self.kwargs.get('pk')
        return get_object_or_404(queryset, cart__user=user, product=product)
