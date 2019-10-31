from django.db import models

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=20)
  birthday = models.CharField(max_length=10)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # 객체 표시 형식 수정
  def __str__(self):
    return f'[{self.pk}] {self.name}'