from django.db import models


class ProductWorkFormat(models.Model):
    """
    Модель формата работы для товара

    Attributes
    ----------
    name : CharField
        Название формата работы

    Methods
    -------
    __str__(self) -> str
        Переопределение метода для вывода формата работы в админ панели
    """

    name = models.CharField(
        'Название формата работы',
        max_length=30,
        unique=True,
    )

    class Meta:
        verbose_name = 'Формат работы'
        verbose_name_plural = 'Форматы работы'

    def __str__(self) -> str:
        return self.name


class ProductIndustry(models.Model):
    """
    Модель сферы деятельности для товара

    Attributes
    ----------
    name : CharField
        Название сферы деятельности

    Methods
    -------
    __str__(self)
        Переопределение метода для вывода сферы деятельности в админ панели
    """

    name = models.CharField(
        'Название сферы деятельности',
        max_length=30,
        unique=True,
    )

    class Meta:
        verbose_name = 'Сфера деятельности'
        verbose_name_plural = 'Сферы деятельности'

    def __str__(self) -> str:
        return self.name
