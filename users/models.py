from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    # ---- Setting a 1 to 1 relation
    user = models.OneToOneField(User, on_delete=models.CASCADE) # When the user is deleted, so is the profile
    # ForeignKey: can be many to one or one to one relationship. The User can have one or more of said thing
    # OneToOneField: one to one relationship. Each User will have only one Profile, 
    #   and that Profile will be associated with only one User
    # models.CASCADE makes so that when the Profile is set to be deleted when the User gets deleted
    # but when we delete the Profile, we wont delete the User, so it's a one way thing. 
    # Why would it be one way thing then?

    # ---- Items to be held in the account:
    profile_picture = models.ImageField(default="default_profile_picture.jpg", upload_to='profile_pics/')
    profile_banner = models.ImageField(default="default_profile_banner.jpg", upload_to="profile_banners/")

    # ---- Dunder functions
    def __str__(self):
        return f'{self.user.username} Profile'


# After making migrations to the database, let's update the users.admin.py