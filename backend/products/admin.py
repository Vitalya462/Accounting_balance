from django.contrib import admin

from .models import Product

admin.site.empty_value_display = 'Не задано'


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    """
    Класс для отображения продуктов в админ панели.

    Attributes
    ----------
    search_fields: tuple[str]
        Поля поиска продуктов
    """

    search_fields = ('title',)
