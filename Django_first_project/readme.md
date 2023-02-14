this all in first_project  file 1 to 6
1. 
__int__.py
this  is a blank python script that dur to its special name let's 
python know that this directry can be treated as a package.

2. 
settings.py
this is where you will store all your project settings.

3. 
urls.py
this is a python script that will store all the project. basically the different pages of your web application.

4. 
wsgi.py
this is a pyhton script that acts as the web server Gateway interface . it will later on help us deploy our web app to production.

5. 
manage.py
this is a pyhton script that we will use a lot .it will be associates with many commands as we build our web app!

6. 
Let use manage.py now
. pyhton manage.py runserver.

you will see a bunch of stuff but at the bottom you see something like.
Django version.

for activate django in terminal type
activate MyDjangoEnv 
ant enter and in will show 
(MyDjangoEnv) c:\etc\etc\etc\thefilenamedoyouhave> 

for run in terminal first  see the folder is there otherwise cd what folder do you have put and enter and afet that 
pythin manage.py runsurver 
and hit enter . 
In terminal there should come one link like this = http://127.0.0.1:8000/
this link put in your browser and run congratulation will come.


next howw to run django application./////////////


now in first_app now see in fisrt_app file we have many file like
1. 
__init__.py
this  is a blank python script that dur to its special name let's 
python know that this directry can be treated as a package.

2. 
admin.py
you can register your models here which Django will then use them with Django's admin interface.

3. 
apps.py
here you can place application specific configuration

4. 
models.py
here you store the application's data models

5. 
tests.py
here you can store test functions to test your code

6. 
views.py
this is where you have funtions that handle requests and return responses.

In first_app we have migrations
this directory stores database specific information as it relates to the models

