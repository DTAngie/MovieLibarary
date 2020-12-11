from django.db import models
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

    def __srt__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'movie_id': self.id})