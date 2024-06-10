1.create a virtual environment
--   pipenv install django

pipfile is like package.json for javascript projects
packages is the packages it is dependent upon
django=* (latest version of django)

2. we need to activate virtual environment
use the python interpreter-
--   pipenv shell

3.use command  -to start new project
--   django-admin 
utililty that comes with django -shows all commands that can be used with django


4.
--   django-admin startproject  storefront
on running the above command it creates a folder storefront that 
has another directory storefront that has core of application

to tell django to use current directory as project directory use period
this wont create an additional directory in the project
-- django-admin startproject storefront .

 5.
 __init__ file defines directory as a package
 settings module defines appl settings
 url module - urls of application
 asgi and wsgi used for deployment

 6.manage.py is a wrapper around django admin
 instead of using djangoadmin use manage.py(takes settings of project into acc)

 7. if u run django-admin runserver u get error saying
 settings arent configured hence we use manage.py
 now run this to find same commands django afmin provides
-- python manage.py 

8.
 -- python manage.py runserver 9000
 9000 is port number(optional) by default port 8000 used
 output
Starting development server at http://
go to it ctrl + click
stop it ctrl +C

9.using the virtual env interpreter and not the python interpreter
$ pipenv --venv
C:\Users\ANUSHA\.virtualenvs\storefront-nmpvfGN
view -> command pallate-> type python interpreter_. enter interpreter path-> paste it
paste this path into enter interpreter path
C:\Users\ANUSHA\.virtualenvs\storefront-nmpvfGNq\bin\python\Scrips\python.exe

C:\Users\username\.virtualenvs\myDjangoProject-y6mANNT9\Scripts\python.exe

10. to create json
For Windows users:
INTERPRETER:
In the virtual environment folder, instead of "bin" folder we have "Script" folder.
PYTHON INTERPRETER:
You must provide full path to the python executable - i.e.: C:\Users\username\.virtualenvs\myDjangoProject-y6mANNT9\Scripts\python.exe"
MISSING .vscode FOLDER:
Using command pallete, open "Open Workspace Settings (JSON)". This will force .vscode folder to appear.

11.
apps =evy django project is collection of apps providing certain functionality
installed apps in setting file
apps in django
admin- admin interface
auth- authenticatin
sessions-old-temp mem on server for managinf users data
messages-to show one time notifications to usr
ststaic files -imgs 
can create your own apps

12.
run server -python manage.py runserver (on one terminal)
python manage.py startapp playground  (on 2nd terminal call it playground)

13.
Every django app has the same structure
migrations folder for generating database tables

admin module- how admin interface for the app is going to look like
apps module to configure apps

models- define model classes for app(define model classes for the apps)
to  plug data from databases and present to username

tests - unit tests

views- req handler(not same as frontend)

14
everytime u create an app add it to installed in settings file

what user sees in django is called template

WRITING VIEWS
view takes req returns resp
called application request handler

add url file
 

  USING templateuser sees this
  to return html content
  add new folder called templates in playground

DEBUGGING Django API
line by line running of application

