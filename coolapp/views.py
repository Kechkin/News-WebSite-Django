from django.http import HttpResponse
from django.shortcuts import render

from coolapp.models import News


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': "Список новостей"
    }
    return render(request, "coolapp/index.html", context)
