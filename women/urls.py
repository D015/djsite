from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    # int str slug uuid path
    path('cats_old/', categories_old, name='categories_old'),  # http://127.0.0.1:8000/cats_old/
    path('cats/<int:catid>/', categories, name='categories'),  # http://127.0.0.1:8000/cats/1/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='archive'),  # http://127.0.0.1:8000/cats/
]