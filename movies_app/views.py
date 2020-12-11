from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.views.generic import ListView, CreateView


class MovieList(ListView):
    model = Movie
    template_name = 'movies/index.html'


class MovieCreate(CreateView):
    model = Movie
    fields = '__all__'

def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

# def movies_index(request):
#     movies = Movie.objects.all()
#     return render(request, 'movies/index.html', {'movies': movies})

def movies_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})