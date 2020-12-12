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
]