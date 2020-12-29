# Step 1
conda create --name myDjangoEnv django
# then say yes with y

# Step 2 make sure it is there ist enviornment
conda info --envs

# Step 3
activate MyDjangoEnv

# step 4 install Django
conda install django

##########################################################
#END OF VIRTUAL ENV SET UP

#Step 5  # create project
django-admin startproject learning_users

#step 6 change directory to the projectname
cd learning_users

#step7 start an app
django-admin startapp basic_app

# next add basic_app in templaes for settings.py

# next type python manage.py migrate

# next python manage.py makemigrations basic_app

#python -m pip install --upgrade pip

# for encription
# next pip install bcrypt
#next pip install django[argon2]

# next in settings right above AUTH_PASSWORD_VALIDATORS
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',

]

# next {
    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    'OPTIONS':{'min_length':9}
},

# next
# Step 11 in settings
import os
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")

# next make static folder
#next make media folder
     # next in media make profile_pics


# next
# Step 13 add this into TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#next
ALLOWED_HOSTS = ['localhost', '127.0.0.1',]


# next
# step 12 make databases look like this
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':os.path.join(BASE_DIR,'db.sqlite3'), # ADD THIS TO THE FILE
        #'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# next
STATIC_DIR = os.path.join(BASE_DIR,'static')
MEDIA_DIR = os.path.join(BASE_DIR,'media')

# Next
STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR,]

MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

# next in models.py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)
# make folder under media named profile_pics
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username


# next pip install pillow (for pictures)

# next under basic_app make file named forms.py
from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')


# next in admin.py
from django.contrib import admin
from basic_app.models import UserProfileInfo
# Register your models here.

admin.site.register(UserProfileInfo)


# next type python manage.py migrate

# next python manage.py makemigrations basic_app

# next type python manage.py migrate

# next in templates folder make new folder basic_app
# in basic_app make (base.html, index.html, login.html, registration.html )

# in base.html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
  </head>
  <body>
    <nav class= 'navbar navbar-default navbar-static-top'>
      <div class="container">
        <ul class= "nav navbar-nav">
          <li><a class="navbar-brand" href="{% url 'index' %}">DJANGO</a></li>
          <li><a class="navbar-link" href="{% url 'admin:index' %}">Admin</a></li>
          <li><a class="navbar-link" href="{% url 'basic_app:register' %}">Register</a></li>

        </ul>
        </div>
    </nav>

    <div class="container">
      {% block body_block %}
      {% endblock %}
    </div>

  </body>
</html>

# next in index.html
{% extends "basic_app/base.html" %}
{% block body_block %}

<div class="jumbotron">
  <h1>Django Level Five</h1>

</div>

{% endblock %}

#next in registration.html
{% extends 'basic_app/base.html' %}
{% load static %}

{% block body_block %}

<div class="jumbotron">
  {% if registered %}
    <h1>Thank you for registering!</h1>
  {% else %}
    <h1>Register Here!</h1>
    <h3>Fill out the form: </h3>

    <form enctype="multipart/form-data" method="post" >
      {% csrf_token %}
      {{ user_form.as_p }}
      {{ profile_form.as_p }}
      <input type="submit" name="" value="Register">

    </form>

  {% endif %}

</div>
{% endblock %}


# next in urls.py under learning_users
from basic_app import views
from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('basic_app/', include('basic_app.urls'))
]

# next under basic_app make new file urls.py
from django.conf.urls import url
from basic_app import views

# Template tagging
app_name = 'basic_app'

urlpatterns = [
    url(r'^register/$',views.register,name='register'), # gives you relative view in url
]


#next go to views.py
from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm
# Create your views here.

def index(request):
    return(request,'basic_app/index.html')

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save() # sending user form to database
            user.set_password(user.password) # hasing the password
            user.save() # saving hash value to databases

            profile = profile_form.save(commit=False)
            profile.user = user # same as model.py

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basic_app/registration.html',{'user_form': user_form,'profile_form':profile_form,'registered':registered})





# create super user
python manage.py createsuperuser


# next in settings.py AT BOTTOM
LOGIN_URL = '/basic_app/user_login'

# next in login.html
{% extends 'basic_app/base.html'%}
{% block body_block %}

<div class="jumbotron">
  <h1>Please Login </h1>
  <form action="{% url 'basic_app:user_login' %}" method="post">
    {% csrf_token %}
    <label for="username">Username:</label>
    <input type="text" name="username" value="Enter Username">

    <label for="password">Password:</label>
    <input type="password" name="password" >

    <input type="submit" name="" value="Login">
  </form>

</div>

{% endblock %}

# next in views.py
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout

@login_required
def special(request):
    return HttpResponse("you are logged in, nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password = password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request,'basic_app/login.html',{})


# next in urls.py in project (learning_users)
path('logout/',views.user_logout,name='logout'),
path('special/',views.special,name='special')
]


# next urls.py learning_users
    url(r'^user_login/$',views.user_login,name='user_login'),

# next in base.html

          {% if user.is_authenticated %}
            <li><a class = 'navbar-link' href = "{% url 'logout' }">Logout</a></li>
          {% else %}
            <li><a class="navbar-link"href="{% url 'basic_app:user_login'%}">Login</a></li>
          {% endif %}



#Deactivate when done
#deactivate MyDjangoEnv

# remove virtual ENVIRONMENT
#conda remove -n MyDjangoEnv --all
