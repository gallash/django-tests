from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm # Obviously creating forms. Default Django form
from django.contrib import messages # flash messages for warnings, debug, error, info and success
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm # Importing from new Forms.py from the current folder. Dev created


# Create your views here.


def register(request):
    # form = UserCreationForm() # This alone will return a new, blank form. 
    # We need to work more with the data passed as the form
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # Created Form
        if form.is_valid():
            form.save() # saving the form. In this case, saving the new user
            username = form.cleaned_data.get("username") # form.cleaned_data is where the validated data is stored
            messages.success(request, f"Account Created Successfully, {username}!")
            # After putting the 'messages' here, make sure to add that to the base html, for it will appear 
            # on any page we open

            return redirect('login') # On successful user creation, redirect user to Login page

    else:
        form = UserRegisterForm() # GET, for example. It needs a blank form
        # This 'register' function is run each time the user interacts with the page:
        #   a) by accessing the page (GET)
        #   b) by submitting a user registration (POST)

    context = {'form': form}
    return render(request, 'users/register.html', context=context) # or, 
    # # substitute 'context=context' by '{'form': form}'

@login_required
def profile(request):
    # This page needs to be accessible ONLY to users who are logged in
    # Hence the use of a decorator called ''
    return render(request, 'users/profile.html')









# As I have not written a explicit view for Login and Logout accesses, I have to change the behaviour of the
# LoginView in the settings.py file by doing:
#   LOGIN_REDIRECT_URL = <name of the page> (e.g. 'website-postings')
# otherwise, Django will attempt to redirect the user to the default page Django expects ('/account/profile'), 
# which might not be in the plans for the project



# How do I separate an Admin account from a regular User account? By creating new Form with boolean value?
# Creating different forms
# Creating new User classes




# I can modify the forms to be a lot nicer looking
# One of the way I can do that is using Crispy Forms for Django
# First, install it: 'pip install django-crispy-forms'
#
# Then, tell Django it is going to be an Installed App (settings.py)
#   'crispy-forms'
# Then, also in settings.py, specify which version of bootstrap are we going to use
#   CRISPY_TEMPLATE_PACK = 'bootstrap4'
#
# After that, go in the HTML page (here it is register.html) and load crispy at the top of the file
#   '{% load crispy_forms_tags %}'
# This allows using Crispy filters in any of our forms
# Then, go in the {{ form }} and add a Django Template filter:
#   {{ form|crispy }}
# 
# But how do I style it to my heart's content?