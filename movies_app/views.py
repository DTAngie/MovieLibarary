from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


# movies = [
#   Movie('Matrix', 1999, 'Wachowski', 'Sci-Fi'),
#   Movie('Klaus', 2019, 'Sergio Pablos', 'Holiday'),
#   Movie('Toy Story', 1995, 'John Lassiter', 'Family')
# ]

def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def movies_index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

def movies_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})