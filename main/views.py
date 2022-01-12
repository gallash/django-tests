from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
# *** Remember, 'render' will look inside './main/templates/' ***


# Home page
def index(response):
    return render(response, 'main/index.html')

# Postings page
def postings(response):
    #return HttpResponse("<h2>This is another page of the Django tutorial I am following</h2>")

    # 'context' is the keyword I have to assign the data created above, in order to be passed in render
    context = {
        # 'posts': posts, # This posts is dummy data
        # while 'posts' is the keyword, posts is the list of dicionaries above
        # I could obviously pass more data in form of dictionaries here, if I had the need to
        'posts': Post.objects.all(), # queries the database for all posts
        'title': 'postings'
    }
    return render(response, 'main/postings.html', context)




# Dummy data (in the form of dictionary), to illustrate how to display data in a page
# posts = [ # List of dictionaries, because this dummy data simulates queries of data which are in the form of dict
#     {
#         'author': "Phillip Gallas",
#         'title': "Welcome to my webpage",
#         'content': "This page is my portfolio. I will show my projects here",
#         'date': "dec/16/2021"
#     },
#     {
#         'author': "Phillip Gallas",
#         'title': "How I created this webpage",
#         'content': "Using Django, I was able to create the backend of this website",
#         'date': "dec/17/2021"
#     },
#     {
#         'author': "Camilla Gallas",
#         'title': "Princess",
#         'content': "My castle",
#         'date': "11/11/2050"
#     }
# ]
