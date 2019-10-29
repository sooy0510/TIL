# 라우팅 역할을 해주는 lib import
from django.urls import path, include
from . import views

urlpatterns = [
  path('index/', views.index),
]