from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.index, name='index'),
    path('students/new/', views.new, name='new'),
    path('students/create/', views.create, name='create'),
]
