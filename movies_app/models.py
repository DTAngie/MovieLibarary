from django.db import models
from django.urls import reverse

# Create your models here.
AWARDS = (
    ('O', 'Oscar'),
    ('A', "Academy Award"),
    ('S', 'Screen Actors Guild'),
)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'movie_id': self.id})

    def is_popular(self):
        return self.award_set.all().count() > 2

class Award(models.Model):
    year = models.IntegerField()
    category = models.CharField(max_length=100)
    name = models.CharField(
        max_length=1,
        choices=AWARDS,
        default=AWARDS[0][0]
    )

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_award_display()} on {self.date}"
    
    class Meta:
        ordering = ['-year']