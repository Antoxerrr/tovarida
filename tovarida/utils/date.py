import datetime
from typing import Union

from django.conf import settings


def format_date(_date: Union[datetime.date, datetime.datetime]) -> str:
    """Возвращает дефолтный формат даты строкой."""
    return _date.strftime(settings.DATE_FORMAT)


def format_datetime(_datetime: datetime.datetime) -> str:
    """Возвращает дефолтный формат даты и времени строкой"""
    return _datetime.strftime(settings.DATETIME_FORMAT)
