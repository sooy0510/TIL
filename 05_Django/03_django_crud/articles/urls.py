# 라우팅 역할을 해주는 lib import
from django.urls import path, include
# 현재 위치에 있는 모든 view들을 가져오자
from . import views

urlpatterns = [
  path('', views.index), 
  path('new/', views.new), 
  path('create/', views.create), 
  path('<int:article_pk>/', views.detail), 
]