# CREATE VIRTUAL ENVIRONMENT !!!!!!!!!!!!!!!!!!!!!!!!!!!!
###############################################################################################################################################
# make a virtual enviornment with (conda create --name myDjangoEnv django)  the enviornment is DjangoMyEnv and the  theing loaded is django
#conda create --name myDjangoEnv django
# say no to load thing
# conda create --name MyDjangoEnv python=3.5
# then say yes with y

# List Envirnments
#conda info --envs

# ACTIVATE ENVIRONMENT
#activate MyDjangoEnv

#Deactivate when done
#deactivate MyDjangoEnv

# remove virtual ENVIRONMENT
conda remove -n MyDjangoEnv --all
###############################################################################################################################################
# Now that i am working in an virtual environment i can install django into the ENVIRONMENT
# This will only be installed in virtual environment
conda install django  # then say yes

# confirm if virtual env is working correctly
###############################################################################################################################################
# start django first project
# see it is installed (django-admin)
#create first project(django-admin startproject first_project)

# The folders means
#__init__.py (this means blank python script this directory can be treated as package)
#asgi.py (this is a python script that acts as a web server gateway interface then will help us deploy our web app to production )
#settings.py)(this is all the project settings)
#urls.py( this will store all url patters for project all the different web pages of the application and how they should connecct to end user)
#wsgi.py()
#manage.py(associated with many of our commands that we use alot)

# now run This
# python manage.py runserver (in this case python first_project/manage.py runserver)
# This starts a development server in url and you can copy and paste into your url .
# use cd first_project to get to the directory that firt_project is working in
