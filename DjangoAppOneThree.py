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
#django-admin startproject projectname

#step 6 change directory to the projectname
#cd projectname

#step7 start an app
python manage.py startapp appname

# step 8
# go to views and type
from django.http import HttpResponse
def index(request):
    return HttpResponse("TEXT TO BE INSERTED")

# Step 9
# Go to url and insert sthis
from appname import views
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]

# step 10
# adit settings add
appname into INSTALLED_APPS

# last step
python manage.py runserver
