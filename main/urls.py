# Paths to webpages inside the project (different views)

from django.urls import path
from . import views 
# The '.' dot represents que current directory where we're in
# By importing from 'views.py', we are importing the views' functions as pages

urlpatterns = [
    path("", views.index, name="website-index"), # path 0. str = "" means home page
    path("postings/", views.postings, name="website-postings"),
]