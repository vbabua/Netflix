from django.contrib import admin
from .models import Movie

# Registers the Movie model with the Django admin site, enabling admin management for this model.
admin.site.register(Movie)
