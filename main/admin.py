from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post) # Importing the 'Post' model above and 
# placing it here will allow us to see and edit 
# the Posts from the Admin page
# Also need to connect the views.py to the actual data (database), and not the dummy data