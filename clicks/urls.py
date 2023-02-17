# -*- coding: utf-8 -*-
from django.urls import path
from .views import *

app_name = 'clicks'

urlpatterns = [
    path('', clicks_view, name='clicks')    
]
