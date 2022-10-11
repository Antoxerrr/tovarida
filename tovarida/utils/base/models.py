from django.db import models

from utils.date import format_date, format_datetime


class BaseModel(models.Model):
    """Базовая модель таблицы БД."""

    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата изменения', auto_now=True)

    def created_verbose(self, as_date=False):
        f = format_date if as_date else format_datetime
        return f(self.created)

    def updated_verbose(self, as_date=False):
        f = format_date if as_date else format_datetime
        return f(self.updated)

    class Meta:
        abstract = True
