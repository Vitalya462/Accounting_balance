from datetime import datetime

from django.shortcuts import render
from django.views.generic import ListView, DetailView


def page_not_found(request, exception):
    return render(request, 'errors/404.html', status=404)


def server_error(request):
    return render(request, 'errors/500.html', status=500)


def csrf_failure(request, reason=''):
    return render(request, 'errors/403csrf.html', status=403)


description = '1) оформление первичных документов, определение первоначальной стоимости и отражение в бухгалтерском учёте.\n 2) расчет и начисление износа, корректировка при изменении срока полезного использования. \n 3) проведение переоценки ОС с отражением дооценки/уценки в балансе. \n 4) разграничение затрат на ремонт и модернизации, корректное отражение в учёте. \n 5) организация сверки фактического наличия ОС с данными учета, выявление излишков или недостатков. \n 6) оформление документов при ликвидации, продаже или передаче ОС, отражение финансового результата. \n 7) контроль соответствия бухгалтерского и налогового учета. \n 8) формирование данных для бухгалтерской и налоговой отчётности.'


services = [
    {
        'id': 1,
        'title': 'Основные средства',
        'description': description,
        'image': 'https://mimigram.ru/wp-content/uploads/2020/07/chto-takoe-foto.jpg',
        'price': 1234,
        'created_at': datetime.now(),
        'work_format': None,
        'industry': None,
        'status': 'A',
        'code': 123,
    },
    {
        'id': 2,
        'title': 'Запасы',
        'description': description,
        'image': 'https://mimigram.ru/wp-content/uploads/2020/07/chto-takoe-foto.jpg',
        'price': 1234,
        'created_at': datetime.now(),
        'work_format': None,
        'industry': None,
        'status': 'A',
        'code': 123,
    },
    {
        'id': 3,
        'title': 'Уставный капитал',
        'description': description,
        'image': 'https://mimigram.ru/wp-content/uploads/2020/07/chto-takoe-foto.jpg',
        'price': 1234,
        'created_at': datetime.now(),
        'work_format': None,
        'industry': None,
        'status': 'A',
        'code': 123,
    },
    {
        'id': 4,
        'title': 'Долгосрочные кредиты и займы',
        'description': description,
        'image': 'https://mimigram.ru/wp-content/uploads/2020/07/chto-takoe-foto.jpg',
        'price': 1234,
        'created_at': datetime.now(),
        'work_format': None,
        'industry': None,
        'status': 'A',
        'code': 123,
    },
]

bid = {}


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
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        try:
            pk = int(pk)
        except (TypeError, ValueError):
            raise RuntimeError

        for service in services:
            if service['id'] == pk:
                return service

        raise RuntimeError

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_items_count'] = len(bid)
        return context
