from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.urls import include, path, reverse_lazy
from django.views.generic.edit import CreateView
from debug_toolbar import urls as debug_toolbar_urls


urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        include('pages.urls')
    ),

    path(
        '',
        include('cart.urls'),
    ),

    path(
        'auth/',
        include('django.contrib.auth.urls')
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'
