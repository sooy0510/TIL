# 라우팅 역할을 해주는 lib import
from django.urls import path, include
# 현재 위치에 있는 모든 view들을 가져오자
from . import views

app_name = 'jobs'
urlpatterns = [
  # 일반적으로 view함수와 똑같이 name바꿈
  path('', views.index, name='index'),    # READ Logic - Index
  path('new/', views.new, name='new'),   
  path('past_job/', views.past_job, name='past_job'),   
]