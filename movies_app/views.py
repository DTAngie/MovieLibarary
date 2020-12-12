from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie, Performer
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
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
    cast_movie_doesnt_have = Performer.objects.exclude(id__in = movie.cast.all().values_list('id'))
    award_form = AwardForm()
    return render(request, 'movies/detail.html', {
        'movie': movie,
        'award_form': award_form,
        'cast': cast_movie_doesnt_have 
    })

def add_award(request, movie_id):
    form = AwardForm(request.POST)
    if form.is_valid():
        new_award = form.save(commit=False)
        new_award.movie_id = movie_id
        new_award.save()
    return redirect('detail', movie_id=movie_id)

def assoc_cast(request, movie_id, performer_id):
    Movie.objects.get(pk=movie_id).cast.add(performer_id)
    return redirect('detail', movie_id=movie_id)

class PerformerList(ListView):
  model = Performer

class PerformerDetail(DetailView):
  model = Performer

class PerformerCreate(CreateView):
  model = Performer
  fields = '__all__'

class PerformerUpdate(UpdateView):
  model = Performer
  fields = '__all__'

class PerformerDelete(DeleteView):
  model = Performer
  success_url = '/performers/'