from datetime import datetime

from django.shortcuts import render
from django.views.generic import ListView, DetailView


def page_not_found(request, exception):
    return render(request, 'errors/404.html', status=404)


def server_error(request):
    return render(request, 'errors/500.html', status=500)


def csrf_failure(request, reason=''):
    return render(request, 'errors/403csrf.html', status=403)


services = [
    {
        'id': 1,
        'title': 'Первая услуга',
        'description': 'Описание первой услуги',
        'image': '',
        'price': 1234,
        'created_at': datetime.now(),
        'work_format': None,
        'industry': None,
        'status': 'A',
        'code': 123,
    }
]

bid = []


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

    template_name = "pages/index.html"
    context_object_name = "product_list"
    paginate_by = 12

    def get_queryset(self):
        """
        Метод для фильтрации по запросу.

        Returns
        -------
        list[Product]
            Список продуктов, соответствующих критериям поиска
            или всем продуктам, если поисковый запрос не указан
        """

        query = self.request.GET.get('search')
        queryset = services

        if query:
            queryset = [
                *filter(
                    lambda service: query in service['title'],
                    queryset,
                )
            ]

        return queryset

    def get_context_data(self, **kwargs):
        """
        Добавляем количество товаров в корзине в контекст.
        """
        context = super().get_context_data(**kwargs)

        context['cart_items_count'] = len(bid)
        return context


class ServiceDetailView(DetailView):
    template_name = 'pages/product_detail.html'
    pk_url_kwarg = 'product_id'

    def get_context_data(self, **kwargs):
        """
        Добавляем количество товаров в корзине в контекст.
        """
        context = super().get_context_data(**kwargs)

        context['cart_items_count'] = len(bid)
        return context
