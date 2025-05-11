from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from products.models import Product
from .enums import CartStatus


User = get_user_model()


class Cart(models.Model):
    """
    Модель корзины пользователя

    Attributes
    ----------
    user: OneToOneField
        Владелец корзины

    Methods
    -------
    __str__(self) -> str
        Переопределение метода для вывода корзины в админ панели
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='Владелец корзины',
    )

    status = models.CharField(
        'Статус корзины',
        choices=CartStatus,
        default=CartStatus.DRAFT,
    )

    created_at = models.DateTimeField(
        'Добавлено',
        auto_now_add=True
    )

    formed_at = models.DateTimeField(
        'Сформировано',
        null=True,
        default=None
    )

    finished_at = models.DateTimeField(
        'Завершено',
        null=True,
        default=None,
    )

    moderator = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='moderator',
        verbose_name='Модератор',
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Корзина {self.user.username}'

    def save(self, *args, **kwargs):
        if self.status == CartStatus.FORMED and not self.formed_at:
            self.formed_at = timezone.now()
        if (self.status == CartStatus.COMPLETED or self.status == CartStatus.REJECTED) and not self.finished_at:
            self.finished_at = timezone.now()

        return super().save(*args, **kwargs)


class CartItem(models.Model):
    """
    Модель товара в корзине

    Attributes
    ----------
    cart: OneToOneField
        Корзина, к которой относится товар
    product: ForeignKey
        Продукт, относящийся к корзине
    quantity: PositiveIntegerField
        Количество продукта в корзине
    """

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Корзина',
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт',
    )

    quantity = models.PositiveIntegerField(
        'Количество товара',
        default=1,
    )

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def __str__(self) -> str:
        return f'{self.product.title} (x{self.quantity})'
