from django.shortcuts import render

from ..models import Task


# DJANGO SIMPLE MVT VIEWS
def list_todo(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "todo/list.html", context)
