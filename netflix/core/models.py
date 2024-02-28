from django.db import models
import uuid
from django.conf import settings

class Movie(models.Model):
    # Choices for the genre of the movie
    GENRE_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('science_fiction', 'Science Fiction'),
        ('fantasy', 'Fantasy'),
    ]

    uu_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateTimeField()
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    length = models.PositiveIntegerField()
    image_card = models.ImageField(upload_to='movie_images/')
    image_cover = models.ImageField(upload_to='movie_images/')
    video = models.FileField(upload_to='movie_videos/')
    movie_views = models.IntegerField(default=0)

    def __str__(self):
        """Return the movie title as its string representation."""
        return self.title

class MovieList(models.Model):
    # Each MovieList entry links a user to a movie they've added to their list
    owner_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='movie_lists'
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='list_entries')

    def __str__(self):
        """Return a string representation of the movie list entry, showing the owner and the movie title."""
        return f"{self.owner_user}'s list - {self.movie.title}"
