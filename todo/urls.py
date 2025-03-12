from django.urls import include, path

from .views import list_todo

urlpatterns = [
    # API (RestFramework) urls
    path("api/", include("todo.api.urls")),
    # Simple django view
    path("list/", list_todo, name="list_todo"),
]
