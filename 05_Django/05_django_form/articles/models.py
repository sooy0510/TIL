from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=40)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True) 
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  # 객체 표시 형식 수정
  def __str__(self):
    return f'[{self.pk}] {self.title}'


class Comment(models.Model):
  # Comment -> 이중 1:N 관계 (Article, User)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  content = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  # Model Level에서 메타데이터 옵션 설정 -> 정렬 가능
  class Meta:
    ordering = ['-pk',]

  def __str__(self):
    return f'[{self.pk}] {self.content}'
  