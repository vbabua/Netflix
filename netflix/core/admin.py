from django.contrib import admin
from .models import Movie
from .models import MovieList

# Registers the Movie model with the Django admin site, enabling admin management for this model.
admin.site.register(Movie)

# Registers the Movie List model with the Django admin site, enabling admin management for this model.
admin.site.register(MovieList)