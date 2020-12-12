from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('movies/', views.MovieList.as_view(), name="index"),
    path('movies/<int:movie_id>/', views.movies_detail, name='detail'),
    path('movies/create/', views.MovieCreate.as_view(), name='movies_create'),
    path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movies_update'),
    path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movies_delete'),
    path('movies/<int:movie_id>/add_award/', views.add_award, name='add_award'),
    path('performers/', views.PerformerList.as_view(), name='performer_index'),
    path('performers/<int:pk>/', views.PerformerDetail.as_view(), name='performer_detail'),
    path('performers/create/', views.PerformerCreate.as_view(), name='performer_create'),
    path('performers/<int:pk>/update/', views.PerformerUpdate.as_view(), name='performer_update'),
    path('performers/<int:pk>/delete/', views.PerformerDelete.as_view(), name='performer_delete'),
    path('movies/<int:movie_id>/assoc_cast/<int:performer_id>/', views.assoc_cast, name='assoc_cast'),
]