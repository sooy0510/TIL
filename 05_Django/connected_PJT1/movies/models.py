from django.db import models

# Create your models here.
class Movie(models.Model):
  title = models.CharField(max_length=50)
  title_en = models.CharField(max_length=50)
  audience = models.IntegerField()
  # open_date = models.DateField()
  open_date = models.CharField(max_length=15)
  genre = models.CharField(max_length=50)
  watch_grade = models.CharField(max_length=20)
  score = models.FloatField()
  poster_url = models.TextField()
  description = models.TextField()

  def __str__(self):
    return f'[{self.pk}]{self.title}'


class Comment(models.Model):
  # 부모가 삭제되면 참조하는 객체도 삭제한다
  # related_name : 부모 테이블에서 역으로 참조할 때 기본적으로 모델이름_set 형식으로 불러온다.
  # related_name이라는 값을 설정해서 _set 명령어를 임의로 변경할 수 있다.
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE,)
  #related_name='comments')
  content = models.CharField(max_length=250)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # Model Level Metadata 설정
  class Meta:
    ordering = ['-pk',]

  def __str__(self):
      return self.content
  