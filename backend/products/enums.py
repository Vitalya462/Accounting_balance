from django.db import models


class ProductStatus(models.TextChoices):
    ACTIVE = 'A', 'Активный'
    BIN = 'B', 'В корзине'
    ARCHIVE = 'AR', 'Архивный'
