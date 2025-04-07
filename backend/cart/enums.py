from django.db import models


class CartStatus(models.TextChoices):
    DRAFT = 'D', 'Черновик'
    DELETED = 'DEL', 'Удалена'
    FORMED = 'F', 'Сформирована'
    COMPLETED = 'C', 'Завершено'
    REJECTED = 'R', 'Отклонено'
