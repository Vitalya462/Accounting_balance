from django.urls import path, include

from .views import UserLoginView, UserLogoutView, UserRegisterView, UserViewSet

from rest_framework.routers import SimpleRouter

user_router = SimpleRouter()
user_router.register('profile', UserViewSet, basename='profile')

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('registration/', UserRegisterView.as_view(), name='registration'),
    path('', include(user_router.urls))
]
