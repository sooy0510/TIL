from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
  movies = Movie.objects.all()
  context = {'movies':movies}
  return render(request, 'movies/index.html', context)


# 영화정보 생성 Form 
# def new(request):
#   return render(request, 'movies/new.html')

# 영화정보 생성
def create(request):
  # POST 요청일 경우 -> 
  if request.method == 'POST':
    title = request.POST.get('title')
    title_en = request.POST.get('title_en')
    audience = request.POST.get('audience')
    open_date = request.POST.get('open_date')
    genre = request.POST.get('genre')
    watch_grade = request.POST.get('watch_grade')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    movie = Movie(title=title, 
                  title_en=title_en, 
                  audience=audience, 
                  open_date=open_date, 
                  genre=genre, 
                  watch_grade=watch_grade, 
                  score=score,
                  poster_url=poster_url,
                  description=description)
                  
    
    movie.save()
    return redirect('movies:detail', movie.pk)
  # GET 요청일 경우 -> 사용자에게 폼 보여주기
  else:
    return render(request, 'movies/create.html')


# 영화 상세정보를 가져오는 함수
def detail(request, movie_pk):
  print(movie_pk)
  print(movie_pk)
  print(movie_pk)
  print(movie_pk)
  print(movie_pk)
  movie = Movie.objects.get(pk=movie_pk)
  print(movie)
  context = {'movie':movie}
  return render(request,'movies/detail.html', context)

# 영화 수정Form
def edit(request, movie_pk):
  movie = Movie.objects.get(pk=movie_pk)
  context = {'movie':movie}
  return render(request,'movies/edit.html', context)

# 영화 수정
def update(request, movie_pk):
  movie = Movie.objects.get(pk=movie_pk)
  movie.title = request.POST.get('title')
  movie.title_en = request.POST.get('title_en')
  movie.open_date = request.POST.get('open_date')
  movie.genre = request.POST.get('genre')
  movie.watch_grade = request.POST.get('watch_grade')
  movie.score = request.POST.get('score')
  movie.poster_url = request.POST.get('poster_url')
  movie.description = request.POST.get('description')

  movie.save()
  #return redirect(f'/articles/{article.pk}/')
  return redirect('movies:detail', movie.pk)


# 영화 삭제
def delete(request, movie_pk):
  movie = Movie.objects.get(pk=movie_pk)
  movie.delete()
  return redirect('movies:index')