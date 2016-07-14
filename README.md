# Django-Tutorial
A quick introduction and tutorial on Django setup and a basic application

## Setup the environment

> Make sure you have pip and virtualenv installed

### Install pip and virtualenv

pip is a package management system used to install and manage software packages written in Python.

virtualenv is a tool to create isolated Python environments. 

#### Mac Users

	sudo easy_install pip
    sudo pip virtualenv
    
#### Linux Users

	sudo apt-get install python-pip
	sudo apt-get install python-virtualenv
	
#### Windows Users

> ummmm, you have bigger problems to worry about :)
    
### Create a virtual environment

Create an environment using `virtualenv`. 

    virtualenv env
    
> The `env` name can be anything and at any location such as `virtualenv ../venvs/django-basics/`

### Activate the environment

Run the following command to activate the environment

    source env/bin/activate
    
Add the env to the .gitignore file

    echo "/env" > .gitignore

### Install required packages using pip

Create a file called `requirements.txt` and add the following packages to it

    Django
    
Run the following command to recursively `pip install` every package in the file

    pip install -r requirements.txt

## Start a new project

Follow the below and [The Django Tutorial](https://docs.djangoproject.com/en/1.9/intro/tutorial01/) which has a lot more details on every step.

    django-admin.py startproject tangeneer . 
    
> tangeneer all lowercase

> note the . at the end: so it creates it in the current directory   

### Start a new app within the project

    python manage.py startapp hr
    