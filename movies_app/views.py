from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def movies_index(request):
    return render(request, 'movies/index.html', {'movies': movies})