from django.shortcuts import render, redirect
from .models import Movie

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
    poster = request.POST.get('poster')

    movie = Movie(title=title, description=description, poster=poster)
    movie.save()

    return redirect('movies:index')
  else:
    return render(request, 'movies/create.html')

def detail(request, movie_pk):
  movie = Movie.objects.get(pk=movie_pk)
  context = {
    'movie':movie,
  }

  return render(request, 'movies/detail.html', context)

def update(request, movie_pk):
  movie = Movie.objects.get(pk=movie_pk)
  if request.method == 'POST':
    movie.title = request.POST.get('title')
    movie.description = request.POST.get('description')
    movie.poster = request.POST.get('poster')
    movie.save()

    return redirect('movies:detail')

  else:
    context = {
      'movie':movie,
    }

    return render(request, 'movies/update.html', context)


def delete(request, movie_pk):
  movie = Movie.objects.get(pk=movie_pk)
  movie.delete()

  return redirect('movies:index')
  