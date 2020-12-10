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
#django-admin startproject ProFour

#step 6 change directory to the projectname
#cd ProFour

#step7 start an app
#python manage.py startapp appfour

# step 7.5
# go to settings and insert import os

# step 8
# go to views and type
#from django.http import HttpResponse
#def index(request):
#    return HttpResponse("TEXT TO BE INSERTED")

# Step 9
# Go to url and insert sthis
#from appname import views
#urlpatterns = [
#    path('', views.index, name='index'),
#    path('admin/', admin.site.urls),
#]

# step 10
# adit settings add
#appname into INSTALLED_APPS

# step 10.5 make a folder called templates in big folder add html file in

# Step 11
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
    # Old way before video
    #BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #print(os.path.abspath(BASE_DIR))
    #print(BASE_DIR)
TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")

# Step 12 add this into TEMPLATES
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

# step 13 make databases look like this
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':os.path.join(BASE_DIR,'db.sqlite3'), # ADD THIS TO THE FILE
        #'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# step 14 make views like THIS
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'insert_me':"Hello I am from views.py!"}
    return render(request,'appfour/index.html',context = my_dict)

# step 15 make folder in templates
# this is named the first_app or app name

# last step
#python manage.py runserver


#Deactivate when done
#deactivate MyDjangoEnv

# remove virtual ENVIRONMENT
#conda remove -n MyDjangoEnv --all
