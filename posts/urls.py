# -*- coding: utf-8 -*-
from django.urls import path
from .views import *


app_name = 'posts'

urlpatterns = [
    path('', post_list_view, name='posts'),
]
