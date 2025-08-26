from django.shortcuts import render
from django.urls import path

from apps.views import index_view, RegisterCreateView

urlpatterns = [
    path('', index_view, name='index-page'),
    path('create-register/', RegisterCreateView.as_view(), name='create-register')
]