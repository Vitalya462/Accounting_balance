from django.contrib import admin

from . import models


class CartItemInline(admin.TabularInline):
    model = models.CartItem
    extra = 0


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    """Класс для отображения корзины в админ панели."""

    inlines = (CartItemInline,)


admin.site.register(models.CartItem)
