# Fusion Fork: A Bold New World

## TO RUN THE ENTIRE THING IN DOCKER
1. docker build -t=webapp .
2. docker run --rm -p 8000:8000 webapp
3. open http://localhost:8000<br /> 
note: has issues with dockerignore, mkdir, folder permissions, and saved files. working on it, but y'all are welcome to aid in debugging. this issue does not exist when run by django only<br /> 

## Note: env is not synced because there are some OS-specific (and potentially user-specific) quirks. It's much safer to simply make your own venv env and not sync it. <br /> 

## To run the app django-style
Linux Instructions
1. Setup the virtual environment <br /> 
python3 -m venv env
2. Activate the virtual environment <br /> 
source env/bin/activate <br />
pip3 install -r requirements.txt
3. Migrate the assets <br /> 
python3 manage.py migrate
4. run the server <br /> 
python3 manage.py runserver <br /> 

Windows vscode Instructions
1. Set up django-friendly virtual environment<br /> 
in vscode terminal first time running in this environment:<br /> 
python -m venv env
2. Switch to virtual environment<br /> 
in vscode, CTRL + SHIFT + P<br /> 
python: select interpreter<br /> 
select the python venv<br /> 
close and reopen the vscode terminal subwindow
3. Activate the virtual environment<br /> 
in vscode terminal window<br /> 
pip install -r requirements.txt
4. Migrate assets<br /> 
python manage.py migrate
4. Run the server<br /> 
python manage.py runserver<br /> 

------------------------------------------------------------------------------- <br />

* uploads go into the uploads directory with a custom URL <br />
* capstone directory is Django high level support files <br />
* webapp directoy is the django app and full feature layer <br />
* manage.py is how django controls everything- migrating, running the server, making apps etc. <br /> 

notable files include;<br /> 
    webapp/urls.py (handles django links to each page)<br /> 
    webapp/views.py (defines functionality for each page)<br /> 
    webapp/templates/webapp/ (html files for each page)<br /> 
    webapp/modules/ (supporting modules for each page as needed)<br /> 
    
## Other notes<br /> 

some amazing information here<br /> 
https://code.visualstudio.com/docs/python/tutorial-django<br /> 
and here<br /> 
https://github.com/Microsoft/python-sample-vscode-django-tutorial<br /> 

## To add a page<br /> 
Go to webapp
1. add a .html to the webapp with the layout
2. create a link to it in urls.py
3. define it's functionality in views.py
4. if it requires additional long functions, recommend that you add the app to the modules folder and import the callables to views
5. if it requires images or css, put them in static
6. more complex features may require methods in webapp/migrations/0001_initial.py, and matching methods in forms.py and models.py. This appears to be how Django handles handoffs between layers, so for now it's a necessary evil. Refer to the upload segments in each file to see how they work together.

No need to create entire seperate top layer django apps: it's better to use modules in webapp to cut down on our redundant instances<br /> 
No need to make major changes to the capstone folder: only needed to change django settings such as save path location<br /> 

TODO: urls accept regexes; make unique URL routing function with an updated results page<br /> 
TODO: create results subpages<br /> 
TODO: generate graphs on results subpages<br /> 
TODO: save as PDF option which collects results from all subpages<br /> 

remember to python manage.py migrate after you add anything to static<br /> 
feel free to add any more notes as you discover them<br /> 
