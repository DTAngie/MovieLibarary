from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import AwardForm


class MovieList(ListView):
    model = Movie
    template_name = 'movies/index.html'

class MovieCreate(CreateView):
    model = Movie
    fields = '__all__'

class MovieUpdate(UpdateView):
    model = Movie
    fields = ['release_year', 'director', 'genre']

class MovieDelete(DeleteView):
    model = Movie
    success_url = '/movies/'

def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

# def movies_index(request):
#     movies = Movie.objects.all()
#     return render(request, 'movies/index.html', {'movies': movies})

def movies_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    award_form = AwardForm()
    return render(request, 'movies/detail.html', {'movie': movie, 'award_form': award_form})

def add_award(request, movie_id):
    form = AwardForm(request.POST)
    if form.is_valid():
        new_award = form.save(commit=False)
        new_award.movie_id = movie_id
        new_award.save()
    return redirect('detail', movie_id=movie_id)