from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


# def index(request):
#     return HttpResponse("Страница приложения women.")
def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def categories_old(request):
    return HttpResponse("<h1>Статьи по категориям OLD</h1>")


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2020:
        # return redirect("/")  # 302 временный
        # return redirect("/", permanent=True)  # 301 постоянный
        # home - имя из women/urls.py urlpatterns
        return redirect("home", permanent=True)  # 301 постоянный

    return HttpResponse(f"<h1>Архив по категориям</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
