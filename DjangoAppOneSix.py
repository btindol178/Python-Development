# Step 1
#conda create --name myDjangoEnv django
# then say yes with y

# Step 2 make sure it is there ist enviornment
#conda info --envs

# Step 3
#activate MyDjangoEnv

# step 4 install Django
#conda install django

##########################################################
#END OF VIRTUAL ENV SET UP

#Step 5  # create project
#django-admin startproject ProSix

#step 6 change directory to the projectname
#cd ProSix

#step7 start an app
#python manage.py startapp appsix

# step 7.5
# go to settings and insert import os

# step 8
# go to views and type
#from django.http import HttpResponse
#def index(request):
#    return HttpResponse("TEXT TO BE INSERTED")

# Step 9
# Go to url and insert sthis
#from appsix import views
#from django.urls import path
#urlpatterns = [
#    path('', views.index, name='index'),
#    path('admin/', admin.site.urls),
#]

# step 10
# adit settings add
#appsix into INSTALLED_APPS

# step 10.5 make a folder called templates in big folder
#add html file in it


# Step 11 in settings
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
    # Old way before video
    #BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #print(os.path.abspath(BASE_DIR))
    #print(BASE_DIR)
TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")


# step 12 make databases look like this
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':os.path.join(BASE_DIR,'db.sqlite3'), # ADD THIS TO THE FILE
        #'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

# 13.5 in settings do THIS
#DEBUG = True
#ALLOWED_HOSTS = [*]
#or
#ALLOWED_HOSTS = ['localhost', '127.0.0.1',]


# step 14 make views like THIS

from django.shortcuts import render
from django.http import HttpResponse
# Still works but hello i am from from views does not work does not call static
# Create your views here.
def index(request):
    my_dict = {'insert_me':"Hello I am from views.py!"}
    return render(request,'appsix/index.html',context = my_dict)

# step 14.5 put that into html file
# within html file in temples put the insert me in like this
#{{insert_me}}


# step 15 make folder in templates
# this is named the first_app or app name

# step 16 make folder within main project folder ProSix  called static

# step 17 inside of static make a folder called images

# step 18 connect that static file to base directory (go to settings and put in)
#STATIC_DIR = os.path.join(BASE_DIR,"static")
# scroll to the bottom by static_url and put that variable in like this
STATIC_URL = '/static/'
STATICFILES_DIRS = [
STATIC_DIR,
]

# Step 19 try to put the static file in the html
# right under <!DOCTYPE HTML> put THIS
#{% load static %}
# DO NOT DO THIS X DOES NOT WORK {% load staticfiles %}
# then you can add image tag like this pointing to django file
#<img src ="{% static "images/django2.jpg" %}" alt="Uh oh didnt show">

# Step 20 make css as static file
# under static make folder called css
# under that folder make file called mystyle.css
# inside put this (somehting simple)
h1{
  color:red;
}:
# Then in side the html do this
<link rel="stylesheet" href= "{% static "css/mystyle.css" %}" />

# last step
#python manage.py runserver


#Deactivate when done
#deactivate MyDjangoEnv

# remove virtual ENVIRONMENT
#conda remove -n MyDjangoEnv --all
