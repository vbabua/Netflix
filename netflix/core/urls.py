# Import the path function from django.urls to define url paths, and import the views module from the current package
from django.urls import path
from . import views

# List of url patterns that Django will use to match browser URLs to the appropriate view function
urlpatterns = [

    # Define a URL pattern for the root URL ('').
    # When the site's root URL is accessed, Django will execute the views.index function.
    path('', views.index, name = 'index')
]