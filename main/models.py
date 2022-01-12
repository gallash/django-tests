from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # User that listed in Admin page?
from django.db.models.deletion import CASCADE # Mode of deletion

# Create your models here.
# Here we can work with databases.


class Post(models.Model): 
    title = models.CharField(max_length=50)
    content = models.TextField()
    # summary = models.CharField(max_length=100) # If I put, it's bligatory. 
    # In the postings page, I can check if SUMMARY exists

    date = models.DateTimeField(default=timezone.now) # Could it be timezone.now()? I'll test it out in the Python Shell
    # It could also be 'auto_now' or 'auto_now_add', but 
    # 'auto_now' will always update the post date whenever an update or change was made, and
    # 'auto_now_add' will never update the post. The date will be set in stone for the initial publication, per se
    # 'default - timezone' on the other hand, I don't remember exactly why it is like that, but I'll test it out, as Corey Schafer has done
    # Also, I want to test why I have to pass the 'timezone.now' function itself instead of the result of the function 'timezone.now()'

    author = models.ForeignKey(User, on_delete=models.CASCADE) # If the User object that created this post is deleted, CASCADE 
    #sets the post to also be deleted
    # 'ForeignKey' adds a many-to-one relationship  

    def __str__(self) -> str:
        return self.title # When we query the posts in the shell we can see the titles







# class ToDoList(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name


# class Item(models.Model):
#     todolist = models.ForeignKey(ToDoList, on_delete=CASCADE) # Why not simply make an instance of ToDoList?
#     text = models.CharField(max_length=300)
#     complete = models.BooleanField()

#     def __str__(self):
#         return self.text

# Why not make classes Composition? 