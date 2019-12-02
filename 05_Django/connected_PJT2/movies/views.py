from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Rating
from .forms import MovieForm

# Create your views here.
def index(request):
  movies = Movie.objects.all()
  context = {
    'movies':movies,
  }
  return render(request, 'movies/index.html', context)

def index2(request):
  movies = Movie.objects.all()
  context = {
    'movies':movies,
  }
  return render(request, 'movies/index2.html', context)


def create(request):
  if request.method == 'POST':
    form = MovieForm(request.POST, request.FILES)
    if form.is_valid():
      # Binding
      movie = form.save(commit=False)
      movie.user = 1
      movie.save()

    return redirect('movies:detail', movie.pk)
  else:
    form = MovieForm()
    context = {'form':form}
    return render(request, 'movies/create.html', context)

def detail(request, movie_pk):
  movie = Movie.objects.get(pk=movie_pk)
  ratings = movie.rating_set.all()
  context = {
    'movie':movie,
    'ratings':ratings,
  }

  return render(request, 'movies/detail.html', context)



def edit(request, movie_pk):
  movie = get_object_or_404(Movie, pk=movie_pk)
  if request.method == 'POST':
    form = MovieForm(request.POST, request.FILES, instance=movie)
    if form.is_valid():
      movie = form.save()
      return redirect('movies:detail', movie_pk)

  else:
    form = MovieForm(instance=movie)
    context = {'form':form}
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