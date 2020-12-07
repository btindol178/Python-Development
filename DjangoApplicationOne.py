# CREATE VIRTUAL ENVIRONMENT !!!!!!!!!!!!!!!!!!!!!!!!!!!!
###############################################################################################################################################
# make a virtual enviornment with (conda create --name myDjangoEnv django)  the enviornment is DjangoMyEnv and the  theing loaded is django

# Step 1
#conda create --name myDjangoEnv django
# then say yes with y

# Step 2 make sure it is there ist enviornment
#conda info --envs

# Step 3
#activate MyDjangoEnv

# step 4 install Django
#conda install django

# Step 5 create first project
#django-admin startproject first_project

# step 5.5 create first app
#python manage.py startapp first_app

# Step 6 run the server make sure directory is in manage.py folder
# python manage.py runserver (in this case python first_project/manage.py runserver)
#Copy and paste ip into broswer

# When done or if need to remove virtual environment do the following two commands
#Deactivate when done
#deactivate MyDjangoEnv

# remove virtual ENVIRONMENT
#conda remove -n MyDjangoEnv --all

####################################################################################################################################################
# inside the app folder the files mean
########################################
# admin.py(register the models makes admin interface for you are cool)
# apps.py for application specific configuration
# models.py for database configuration
# tests.py made up of a series of function
# views.py where you have functions that handles requests and returns responses
# migrations stores database specific information as related to the models

# Step 7
# In first application file Or first project file and put first_app in the settings then run server to make sure
#'first_app' # we created this app and we need to install it in our settings

# Step 8
# use some simple text
# in views.py enter from django.http import HttpResponse
# Then enter def index(request):    return HttpResponse("Hello World!")

# step 9 go to urls in first project
# do this (from first_app import views)
# then do this: not this

#from django.urls import path
#django.contrib import admin
#from django.conf.urls import url
#from first_app import views

#urlpatterns = [
#    url(r'^$', views.index),
#    url(r'^admin/$', admin.site.urls),
#]
