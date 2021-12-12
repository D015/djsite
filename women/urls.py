from django.urls import path, re_path

from .views import *

urlpatterns = [
    # path('', index, name='home'),
    path('', WomenHome.as_view(), name='home'),
    path('about/', about, name='about'),
    # int str slug uuid path
    # path('cats_old/', categories_old, name='categories_old'),  # http://127.0.0.1:8000/cats_old/
    # path('cats/<int:catid>/', categories, name='categories'),  # http://127.0.0.1:8000/cats/1/
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='archive'),  # http://127.0.0.1:8000/cats/
    # path('addpage/', addpage, name='add_page'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    # path('post/<slug:post_slug>/', show_post, name='post'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    # path('category/<int:cat_id>/', show_category, name='category'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),

]