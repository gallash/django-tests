"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include # 'include' to import main.urls list of paths
from users import views as users_views # It says it doesn't work, but in reality it does --__;)__--
# Below I am importing the libraries to display the medias in Development mode
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include("main.urls")), # 0
    path('register/', include("users.urls")),
    path('profile/', users_views.profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), # 1
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 0. 
# One can reference these pages easily by using the 'name' values in the form:
#   href="{% url 'user-registration' %}", 
#   href="{% url 'website-postings' %}"
# Also, dummy links are passed as #:
#   href="#"

# 1. 
# Why '.as_view()'? 
# Also, note that we can specify which template to use, inside .as_view(), we add the attribute 'tempalte_name'
# and where it's located