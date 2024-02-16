from django.db import models
import uuid
from django.conf import settings

class Movie(models.Model):
    # Define genre choices for the Movie model
    GENRE_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('science_fiction', 'Science Fiction'),
        ('fantasy', 'Fantasy'),
    ]

    # Fields for the Movie model with appropriate data types and constraints
    uu_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Unique identifier for each movie instance
    title = models.CharField(max_length=255)  # Title of the movie
    description = models.TextField()  # Detailed description of the movie
    release_date = models.DateTimeField()  # Release date and time of the movie
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)  # Genre of the movie, chosen from predefined choices
    length = models.PositiveIntegerField()  # Length of the movie in minutes
    image_card = models.ImageField(upload_to='movie_images/')  # Image for movie card
    image_cover = models.ImageField(upload_to='movie_images/')  # Cover image for the movie
    video = models.FileField(upload_to='movie_videos/')  # Video file for the movie
    movie_views = models.IntegerField(default=0)  # Counter for movie views, defaulting to 0

    def __str__(self):
        # String representation of the Movie model, which is the title of the movie
        return self.title
