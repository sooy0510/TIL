from django.contrib import admin
from django.urls import path,include
from . import views

app_name='movies'

urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.new, name='new'),        # CREATE Logic - form전달
    # path('create/', views.create, name='create'),  # CREATE Logic - 생성
    path('create/', views.create, name='create'),   # GET(new) / POST(create)
    path('<int:movie_pk>/', views.detail, name='detail'),
    # path('<int:movie_pk>/edit/', views.edit, name='edit'),
    # path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'), # DELETE Logic
    path('delete/', views.delete, name='delete'),
    path('admin/', admin.site.urls),
    # edit(get/post)
    
]
