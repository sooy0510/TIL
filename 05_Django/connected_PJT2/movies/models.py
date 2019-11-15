from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.db import models

# Create your models here.
class Movie(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()
  poster = ProcessedImageField(
    processors=[Thumbnail(200,300)],  # 처리할 작업
    format='JPEG',                    # 이미지 포맷
    options={'quality':90},           # 각종 추가 옵션
    upload_to='movies/images',      # 저장 위치   
    # 실제경로 -> MEDIA_ROOT/movies/images
  ) 
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.IntegerField(default=1)


class Rating(models.Model):
  score = models.FloatField()
  content = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.IntegerField()
