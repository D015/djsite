from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AddPostForm
from .models import *
from .utils import DataMixin


# def index(request):
#     posts = Women.objects.filter(is_published=True)
#     # cats = Category.objects.all()
#
#     context = {
#         'posts': posts,
#         # 'cats': cats,
#         # 'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#     return render(request, 'women/index.html', context=context)
class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


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


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#
#     return render(request, 'women/addpage.html',
#                   {'form': form, 'title': 'Добавление статьи'})
class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        return dict(list(context.items()) + list(c_def.items()))


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#
#     context = {
#         'post': post,
#         # 'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'women/post.html', context=context)
class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'].title)
        return dict(list(context.items()) + list(c_def.items()))


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


# def show_category(request, cat_id):
#     posts = Women.objects.filter(cat_id=cat_id, is_published=True)
#     if len(posts) == 0:
#         raise Http404()
#     # cats = Category.objects.all()
#
#     context = {
#         'posts': posts,
#         # 'cats': cats,
#         # 'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_id,
#     }
#
#     return render(request, 'women/index.html', context=context)
class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False # выдаёт ошибку если такой категории нет

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'],
                                    is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Категория - ' + str(context['posts'][0].cat.name),
            cat_selected=context['posts'][0].cat_id)

        return dict(list(context.items()) + list(c_def.items()))
