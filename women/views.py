from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *


# def index(request):
#     return HttpResponse("Страница приложения women.")
def index(request):
    posts = Women.objects.filter(is_published=True)
    # cats = Category.objects.all()

    context = {
        'posts': posts,
        # 'cats': cats,
        # 'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    # return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})
    return render(request, 'women/about.html', {'title': 'О сайте'})


# def categories_old(request):
#     return HttpResponse("<h1>Статьи по категориям OLD</h1>")
#
#
# def categories(request, catid):
#     if request.GET:
#         print(request.GET)
#     return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")
#
#
# def archive(request, year):
#     if int(year) > 2020:
#         # return redirect("/")  # 302 временный
#         # return redirect("/", permanent=True)  # 301 постоянный
#         # home - имя из women/urls.py urlpatterns
#         return redirect("home", permanent=True)  # 301 постоянный
#
#     return HttpResponse(f"<h1>Архив по категориям</h1><p>{year}</p>")


def about(request):
    return render(request, 'women/about.html',
                  # {'menu': menu, 'title': 'О сайте'})
                  {'title': 'О сайте'})


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id, is_published=True)
    if len(posts) == 0:
        raise Http404()
    # cats = Category.objects.all()

    context = {
        'posts': posts,
        # 'cats': cats,
        # 'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'women/index.html', context=context)
