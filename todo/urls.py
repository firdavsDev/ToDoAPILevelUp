from django.urls import path

from .views import list_todo

urlpatterns = [
    # Simple django view
    path("list/", list_todo, name="list_todo"),
]
