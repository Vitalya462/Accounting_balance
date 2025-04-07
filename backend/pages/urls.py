from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path(
        '',
        views.IndexListView.as_view(),
        name='index',
    ),
    path(
        'product/<int:product_id>/',
        views.ProductDetailView.as_view(),
        name='product_detail',
    )
]