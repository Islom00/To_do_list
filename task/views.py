
from django.shortcuts import render

from .models import Task
from django.db.models import Q



def index(request):
    q = request.GET.get("q")

    if q:
        data = Task.objects.filter(Q(title__icontains=q))

    else:
        data = Task.objects.all()

    context = {
        "data": data
    }

    return render(request, "index.html", context)
