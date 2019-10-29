# 라우팅 역할을 해주는 lib import
from django.urls import path, include
# 현재 위치에 있는 모든 view들을 가져오자
from . import views

urlpatterns = [
  path('', views.index), 
  path('throw/', views.throw), 
  path('catch/', views.catch), 
  path('art/', views.art), 
  path('result/', views.result), 
  path('user_new/', views.user_new), 
  path('user_create/', views.user_create),
  path('static_sample/', views.static_sample),  
]