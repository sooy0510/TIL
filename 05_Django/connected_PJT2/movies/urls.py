from django.urls import path, include
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
]
