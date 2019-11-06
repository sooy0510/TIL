from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=40)
  content = models.TextField()
  # 원래대로라면 새로운 필드를 추가하고 나면 makemigrations할때, 어떤 값을 넣을건지 Django가 물어본다. 
  # 기본적으로 blank=False이기 때문이다
  # blank = True -> '빈 문자열'이 들어가도 된다
  # image = models.ImageField(blank=True) 
  # Django에서 제공하는 imagefield를 사용하는 것이 아니라 imagekit에서 제공하는 필드 쓸거임
  # 인자들은 바꿔도 migration안해도 됨
  image = ProcessedImageField(
    processors=[Thumbnail(200,300)],  # 처리할 작업
    format='JPEG',                    # 이미지 포맷
    options={'quality':90},           # 각종 추가 옵션
    upload_to='articles/images',      # 저장 위치   
    # 실제경로 -> MEDIA_ROOT/articles/images
  )
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # 객체 표시 형식 수정
  def __str__(self):
    return f'[{self.pk}] {self.title}'


class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  content = models.CharField(max_length=250)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'[{self.pk}] {self.content}'
    