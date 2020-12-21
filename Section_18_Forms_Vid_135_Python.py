# Step 1
conda create --name myDjangoEnv django

# Step 2
activate MyDjangoEnv
conda install django

# Step 3
django-admin startproject basicforms

# Step 4
cd basicforms

# Step 5
python manage.py startapp basicapp

# Step 5
#Create templates folder
    # inside templates folder make folder called (basicapp)
        # make index.html inside that
        # make another html named form_page.html

# Step 6
# Go to settings.py and at top insert this...
import os
from pathlib import Path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")
# in INSTALLED_APPS in settings file add your basicapp to it
'basicapp'
# Go to Templates and put in DIRS:
TEMPLATE_DIR
# GO TO #ALLOWED_HOSTS and put this
 ALLOWED_HOSTS= ['localhost', '127.0.0.1',]
 # go to database and do this ... ( HAVE NOT DONE THIS YET!!!!)
# step 12 make databases look like this
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':os.path.join(BASE_DIR,'db.sqlite3'), # ADD THIS TO THE FILE
        #'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# ALSO PUT THIS IN !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# STATIC_DIR = os.path.join(BASE_DIR,"static")
# # scroll to the bottom by static_url and put that variable in like this
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
# STATIC_DIR,
# ]


# Step 7
# Make new file in basicapp called forms.py
# then add this
# from django import forms
from django import forms
# from django.forms import ModelForm

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

# Step 8
# Now set up the views.py folder
# Put this in ....
from django.shortcuts import render
from . import forms

def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #DO SOMETHING CODE!!
            print("Validation Sucess!")
            print("NAME" + form.cleaned_data['name']) # this comes from forms.py
            print("EMAIL" + form.cleaned_data['email']) # this comes from forms.py
            print("TEXT" + form.cleaned_data['text']) # this comes from forms.py

    return render(request,'basicapp/form_page.html',{'form':form})



# Step 9
# Go to URLs and do this
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
#from basicapp import forms
from basicapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('formpage/', views.form_name_view,name='form_name'),
]


# Step 10
# go to html and insert form
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Forms</title>
  </head>
  <body>
    <div class ="container">
      {{form}} # This part right here!!!!!!!!!!!!
  </body>
</html>

# Step 11 reformat the index html to look like this
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Home</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
  </head>
  <body>
    <div class="container">
      <div class="jumbotron">
        <h1>Welcome to home page!</h1>
        <h2>Go to /formpage to fill out the form</h2>
      </div>
    </div>

  </body>
</html>

# step 12 reformat the form_page html to look like this.
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Forms</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
  </head>
  <body>
    <h1>Fill out the form!</h1>
    <div class ="container">
      <form method="POST">
        {{form.as_p}}
        {% csrf_token %}
        <input type="submit" class = "btn btn-primary" value="Submit">
      </form>

  </body>
</html>
