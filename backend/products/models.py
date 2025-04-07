from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from minio_storage.storage import MinioMediaStorage

from product_components import models as product_component_models
from .enums import ProductStatus


class Product(models.Model):
    """
    Модель продукта.

    Attributes
    ----------
    title : CharField
        Название товара
    description: TextField
        Описание товара
    image: ImageField
        Изображение товара
    price: DecimalField
        Цена товара
    created_at: DateTimeField
        Дата создания товара

    Methods
    -------
    __str__(self)
        Переопределение метода для вывода товара в админ панели
    """

    title = models.CharField(
        'Название',
        max_length=50,
        unique=True,
        blank=False,
    )

    description = models.TextField(
        'Описание',
    )

    image = models.ImageField(
        'Картинка',
        storage=MinioMediaStorage,
    )

    price = models.DecimalField(
        'Цена товара',
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(
                Decimal(0),
                message='Цена не может быть отрицательной',
            ),
        ],
    )

    created_at = models.DateTimeField(
        'Добавлено',
        auto_now_add=True,
    )

    work_format = models.ForeignKey(
        product_component_models.ProductWorkFormat,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Формат работы',
    )

    industry = models.ForeignKey(
        product_component_models.ProductIndustry,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Сфера деятельности',
    )

    status = models.CharField(
        'Статус товара',
        choices=ProductStatus,
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
        return self.title
