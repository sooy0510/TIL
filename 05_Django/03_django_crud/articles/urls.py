# 라우팅 역할을 해주는 lib import
from django.urls import path, include
# 현재 위치에 있는 모든 view들을 가져오자
from . import views

app_name = 'articles'
urlpatterns = [
  # 일반적으로 view함수와 똑같이 name바꿈
  path('', views.index, name='index'),    # READ Logic - Index
  path('new/', views.new, name='new'),  # CREATE Logic - 사용자에게 폼 전달
  path('create/', views.create, name='create'),    # CREATE Logic - 데이터베이스에 저장
  path('<int:article_pk>/', views.detail, name='detail'),  # READ Logic - Detail
  path('<int:article_pk>/delete/', views.delete, name='delete'), # DELETE Logic
  # articles/9/delete 
  path('<int:article_pk>/edit/', views.edit, name='edit'), # UPDATE Logic - 폼 전달
  path('<int:article_pk>/update/', views.update, name='update'), # UPDATE Logic - DB저장
]