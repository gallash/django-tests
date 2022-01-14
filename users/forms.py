from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    # username = forms.CharField(max_length=50)
    # password = forms.PasswordInput()
    email = forms.EmailField(required=True) # attribute: 'required=true' by default
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)



    class Meta:
        # https://www.geeksforgeeks.org/meta-class-in-models-django/
        # The Meta class is already known in the Django Framework
        # Its purpose is to override any pre-existing definitions from the class we are working with
        # So for example,
        
        # Any '.save()' in the context of models using this UserRegisterForm will be saved here
        model = User
        
        # Which fields appear (and in what order) in the Form in the browser
        fields = ['first_name','last_name','username','email','password1','password2'] 
        # theses elements come from the UserCreationForm source
        # I can check out the source code by checking where is Django installed on my Computer 
        # https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/
        # https://docs.djangoproject.com/en/3.2/ref/models/options/
    

# class 