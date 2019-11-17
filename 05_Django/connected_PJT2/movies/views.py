from django.shortcuts import render, redirect
from .models import Movie, Rating

# Create your views here.
def index(request):
  movies = Movie.objects.all()
  context = {
    'movies':movies,
  }
  return render(request, 'movies/index.html', context)


def create(request):
  if request.method == 'POST':
    title = request.POST.get('title')
    description = request.POST.get('description')
    poster = request.FILES.get('poster')  

    movie = Movie(title=title, description=description, poster=poster)
    movie.save()

    return redirect('movies:detail', movie.pk)
  else:
    return render(request, 'movies/create.html')

def detail(request, movie_pk):
  movie = Movie.objects.get(pk=movie_pk)
  ratings = movie.rating_set.all()
  context = {
    'movie':movie,
    'ratings':ratings,
  }

  return render(request, 'movies/detail.html', context)

def edit(request, movie_pk):
  movie = Movie.objects.get(pk=movie_pk)
  if request.method == 'POST':
    movie.title = request.POST.get('title')
    movie.description = request.POST.get('description')
    movie.poster = request.FILES.get('poster')
    movie.save()

    return redirect('movies:detail', movie_pk)

  else:
    context = {
      'movie':movie,
    }

    return render(request, 'movies/update.html', context)


def delete(request, movie_pk):
  movie = Movie.objects.get(pk=movie_pk)
  movie.delete()

  return redirect('movies:index')

def ratings_create(request, movie_pk):
  movie = Movie.objects.get(pk=movie_pk)
  score = request.POST.get('score')
  content = request.POST.get('content')
  rating = Rating.objects.create(movie=movie, score=score, content=content)
  rating.save()
  return redirect('movies:detail', movie_pk)
  

def ratings_delete(request, movie_pk, rating_pk):
  rating = Rating.objects.get(pk=rating_pk)
  rating.delete()
  return redirect('movies:detail', movie_pk)