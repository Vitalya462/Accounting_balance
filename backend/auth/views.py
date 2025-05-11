from rest_framework.generics import CreateAPIView, UpdateAPIView, GenericAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import UpdateModelMixin
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth import login, logout, authenticate

from .serializers import UserRegisterSerializer, UserLoginSerializer, User, UserSerializer
from .authentications import CsrfExemptSessionAuthentication

from drf_spectacular.utils import extend_schema


class UserRegisterView(CreateAPIView):  # POST регистрация
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        login(self.request, user)


class UserLoginView(APIView):  # POST аутентификация
    authentication_classes = (CsrfExemptSessionAuthentication, )
    permission_classes = [AllowAny]

    @extend_schema(request=UserLoginSerializer)
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        username = serializer.initial_data.get('username', None)
        password = serializer.initial_data.get('password', None)
        user = authenticate(
            request=request, username=username, password=password)
        if user:
            login(request, user)
            return Response({"detail": "Успешный вход"})

        return Response({"detail": "Вход не выполнен"}, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):  # POST деавторизация
    authentication_classes = (CsrfExemptSessionAuthentication, )

    def post(self, request):
        logout(request)
        response = Response({"detail": "Успешный выход"},
                            status=status.HTTP_200_OK)
        response.delete_cookie('sessionid')
        return response


class UserViewSet(UpdateModelMixin, GenericViewSet):  # PUT пользователя
    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names = ('put', )
