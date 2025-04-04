import django_filters

from .models import Task


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = {
            "completed": ["exact"],
            "is_public": ["exact"],
            "user": ["exact"],
            # "title": ["exact"], bu birga bir tekshirish uchun
            # "title": ["icontains"],  # ichida borligini tekshiradi
            # start with
            "title": ["istartswith"],  # boshlanishi
        }
