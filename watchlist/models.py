# watchlist/models.py
from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    poster = models.URLField()
    tmdb_id = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.title} ({self.release_year})"

class Watchlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie, through='WatchlistItem')

    def __str__(self):
        return f"{self.user.username}'s Watchlist"

class WatchlistItem(models.Model):
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=0)
    watched = models.BooleanField(default=False)
    rating = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('watchlist', 'movie')
        ordering = ['position']

    def __str__(self):
        return f"{self.movie.title} in {self.watchlist.user.username}'s list"
