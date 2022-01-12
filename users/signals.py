"""
The reason why this file exists is to allow the User to have his/her default profile created 
as soon as their user account is created
In order to do that, the User CREATION will send a SIGNAL, and Django will have to catch that and 
process it accordingly
"""

from django.contrib.auth.models import User
from django.db.models.signals import post_save # signal fired when an object is created?
from django.dispatch import receiver # this is the decorator that receives the signal of an event
from .models import Profile

@receiver(post_save, sender=User) # This decorator receives a signal (here 'post_save') from a class (here, User)
def create_profile(sender, instance, created, **kwargs): # SICK (sender, instance, c, **kwargs) model
    # sender = the Class from which the signal originated
    # instance = the object/instance of the Class that sent the signal
    # created = it's a flag that returns True if signal is received
    # **kwargs = additional keywords
    #
    # Important: Never, in a million years, alter/update/modify any of the instance's fields here in the
    # post_save functions? This is because, any change will be followed by another 'save' method, which thus 
    # results in a signal being sent, which then is caught by the receiver, creating a never ending loop
    
    if created: # if it's True that the instance was CREATED
        Profile.objects.create(user=instance) # why 'user' and not 'username'?