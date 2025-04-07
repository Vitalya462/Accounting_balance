from django.contrib import admin

from . import models


@admin.register(models.ProductWorkFormat)
class WorkFormatAdmin(admin.ModelAdmin):
    """
    Класс для отображения формата работы в админ панели.

    Attributes
    ----------
    search_fields: tuple[str]
        Поля поиска форматов работы
    """

    search_fields = ('name',)


@admin.register(models.ProductIndustry)
class IndustryAdmin(admin.ModelAdmin):
    """
    Класс для отображения сферы деятельности в админ панели.

    Attributes
    ----------
    search_fields: tuple[str]
        Поля поиска сферы деятельности
    """

    search_fields = ('name',)
