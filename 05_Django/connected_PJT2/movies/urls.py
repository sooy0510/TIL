from django.urls import path, include
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('create/', views.create, name='create'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/edit/', views.edit, name='edit'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'), 
    path('<int:movie_pk>/ratings/new/', views.ratings_create, name='ratings_create'), 
    path('<int:movie_pk>/ratings/<int:rating_pk>/delete/', views.ratings_delete, name='ratings_delete'), 
]
