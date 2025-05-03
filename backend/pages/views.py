from django.shortcuts import render
from django.views.generic import ListView, DetailView

from cart.models import CartItem
from products.models import Product


def page_not_found(request, exception):
    return render(request, 'errors/404.html', status=404)


def server_error(request):
    return render(request, 'errors/500.html', status=500)


def csrf_failure(request, reason=''):
    return render(request, 'errors/403csrf.html', status=403)


class IndexListView(ListView):
    """
    Представление, которое отображает список продуктов

    Attributes
    ----------
    model : Type[Product]
        Модель, которую будет отображать представление
    template_name : str
        Название (Путь) шаблона для рендеринга
    context_object_name : str
        Имя контекстной переменной для использования в шаблоне

    Methods
    -------
    get_queryset(self) -> list[Product]
        Возвращает отфильтрованный запрос продуктов
        на основе поискового запроса
    """

    model = Product
    template_name = "pages/index.html"
    context_object_name = "product_list"
    paginate_by = 12

    def get_queryset(self) -> list[Product]:
        """
        Метод для фильтрации по запросу.

        Returns
        -------
        list[Product]
            Список продуктов, соответствующих критериям поиска
            или всем продуктам, если поисковый запрос не указан
        """

        query = self.request.GET.get('search')
        queryset = Product.objects.all()

        if query:
            queryset = queryset.filter(title__icontains=query)

        queryset = queryset.order_by('title')

        return queryset

    def get_context_data(self, **kwargs):
        """
        Добавляем количество товаров в корзине в контекст.
        """
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if not user.is_authenticated:
            return context

        cart_items_count = 0
        cart_items = CartItem.objects.filter(cart__user=user)

        for item in cart_items:
            cart_items_count += item.quantity

        context['cart_items_count'] = cart_items_count
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'pages/product_detail.html'
    pk_url_kwarg = 'product_id'

    def get_context_data(self, **kwargs):
        """
        Добавляем количество товаров в корзине в контекст.
        """
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if not user.is_authenticated:
            return context

        cart_items_count = 0
        cart_items = CartItem.objects.filter(cart__user=user)

        for item in cart_items:
            cart_items_count += item.quantity

        context['cart_items_count'] = cart_items_count
        return context
