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
django-admin startproject ProSeven

#step 6 change directory to the projectname
cd ProSeven

#step7 start an app
python manage.py startapp appseven

# step 7.5
# go to settings and insert
import os

# step 8
# go to views and type
from django.http import HttpResponse
def index(request):
    return HttpResponse("TEXT TO BE INSERTED")

# Step 9
# Go to url and insert sthis
from appseven import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]

# step 10
# adit settings add
#appseven into INSTALLED_APPS
appseven

# step 10.5 make a folder called templates in big folder
#add html file in it


# Step 11 in settings
import os
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
    return render(request,'appseven/index.html',context = my_dict)

# step 14.5 put that into html file
# within html file in temples put the insert me in like this
#{{insert_me}}
{{insert_me}}

# step 15 make folder in templates
# this is named the first_app or app name
appseven

# step 16 make folder within main project folder ProSeven  called static

# step 17 inside of static make a folder called images

# step 18 connect that static file to base directory (go to settings and put in)
STATIC_DIR = os.path.join(BASE_DIR,"static")
# scroll to the bottom by static_url and put that variable in like this
STATIC_URL = '/static/'
STATICFILES_DIRS = [
STATIC_DIR,
]

# Step 19 try to put the static file in the html
# right under <!DOCTYPE HTML> put THIS
{% load static %}
# DO NOT DO THIS X DOES NOT WORK {% load staticfiles %}
# then you can add image tag like this pointing to django file
<img src ="{% static "images/django2.jpg" %}" alt="Uh oh didnt show">

# Step 20 make css as static file
# under static make folder called css
# under that folder make file called mystyle.css
# inside put this (somehting simple)
h1{
  color:red;
}:
# Then in side the html do this
<link rel="stylesheet" href= "{% static "css/mystyle.css" %}" />


# Step 20 go to model.py and put this
# Create your models here.
# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.DO_NOTHING) # CASCADE IS OPTION OTHER THAN DO NOTHING
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.DO_NOTHING)
    date = models.DateField()

    def __str__(self):
        return self(self.date)

#step 21 put this in terminal
python manage.py migrate

# step 22 register migrations to Application
python manage.py makemigrations appseven

# step 23 run migrate one more time and models will be connected to sqlite db
python manage.py migrate

# step 24 can interact with sql database in python through shell...
# in terminal put
python manage.py shell

# step 25 once in python put THIS (just to check that it worked dont do this ever time.......)
from appseven.models import Topic
print(Topic.objects.all()) # you will get nothing need input first_app
# putthis
t = Topic(top_name="Social Network")
t.save()
print(Topic.objects.all()) # now this will print what you put in t.save()
# now we can quit()
quit()

# step 26 in admin.py folder we will work with the step 25 stuff from now on
# put this in
from appseven.models import AccessRecord,Topic,Webpage
#register models
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)

# step 27 make super user so regular joe smoe cant mess with databases
# put this in (make sure your directory in in the project)
python manage.py createsuperuser
# then put in username and password

# Step 28 run admin server to check out the admin file
python manage.py runserver
# front end should look the same
# but when you check out admin part doing this you get login
#http://127.0.0.1:8000/admin
# you will see django admin login

# step 28.5 (dont do this every time )
#python manage.py runserver

# step 29 install Faker library to populate fake stuff into database for instructional purposes
# creates fake data for models folder
pip install Faker
# read documentation ....
# do this next

# step 30 under top level ProSeven folder create new file called
#populate_seventh_app.py

# step 31 inside populate_seventh_app.py put this:
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProSeven.settings')

import django
django.setup()

## Fake pop script
import random
from appseven.models import AccessRecord,Webpage,Topic
from faker import Faker

# make instance of faker object
fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        #Get the topic for the entry
        top =add_topic()

        # create the fake data for the entry
        fake_url = fakegen.url()
        fake_date= fakegen.date()
        fake_name = fakegen.company()

        #create new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # create fake access record for Webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("Populating complete!")

# step 31.5 to check if it runs correctly dothis
python populate_seventh_app.py
# then runserver to check admin!!!
python manage.py runserver
# add/admin and check out webpages!!!!!!



#Deactivate when done
#deactivate MyDjangoEnv

# remove virtual ENVIRONMENT
#conda remove -n MyDjangoEnv --all
