from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.urls import include, path, reverse_lazy
from django.views.generic.edit import CreateView
from debug_toolbar import urls as debug_toolbar_urls

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),

    path(
        'products/',
        include('products.urls')
    ),

    path('carts/', include('cart.urls')),

    path(
        'auth/',
        include('auth.urls')
    ),

    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('pages:index'),
        ),
        name='registration',
    ),

    path(
        '__debug__/',
        include(debug_toolbar_urls)
    ),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
]
