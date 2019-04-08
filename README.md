# v2; webapp features branch

### Note: env should not be synced because there are some OS-specific (and potentially user-specific) quirks. It's much safer to simply make your own venv env (or venv myenv if you so prefer) and not sync it.<br /> 

## To run the app django-style
0. Ensure that you have installed and are using python 3.6.8

Linux Instructions
1. Setup the virtual environment <br /> 
python3 -m venv env
2. Activate the virtual environment <br /> 
source env/bin/activate
3. Install dependencies<br /> 
pip install -r requirements.txt<br /> 
4. run the server <br /> 
python3 manage.py migrate <br /> 
python3 manage.py runserver <br /> 

Windows (vscode) Instructions
1. Setup the virtual environment <br /> 
python -m venv env
2. Activate the virtual environment vscode-style<br /> 
in vscode, CTRL + SHIFT + P<br /> 
python: select interpreter<br /> 
select the python venv<br /> 
close and reopen the vscode terminal subwindow
3. Install dependencies<br /> 
pip install -r requirements.txt<br /> 
4. run the server <br /> 
python manage.py migrate <br /> 
python manage.py runserver <br /> 

------------------------------------------------------------------------------- <br />

* uploads go into the uploads directory with a custom URL <br />
* capstone directory controls all of the URL <br /> 
* dash_results directory is the dash app <br /> 
* upload directoy is the django upload app that links to the dash app <br />
* manage.py is how django controls everything- migrating, running the server, making apps etc. <br /> 

### TO RUN THE ENTIRE THING IN DOCKER (but don't right now, implementation is incomplete)
0. start Docker Desktop
1. docker build -t=webapp .
2. docker run --rm -p 8000:8000 -v uploads:/uploads webapp
3. open http://localhost:8000<br /> 
note: does not give an error message but file does not appear in actual directory; more experimentation required <br /> 

## Other notes<br /> 

some amazing information here<br /> 
https://code.visualstudio.com/docs/python/tutorial-django<br /> 
and here<br /> 
https://github.com/Microsoft/python-sample-vscode-django-tutorial<br /> 
https://bitbucket.org/m_c_/sample-dash/overview<br /> 
https://buildmedia.readthedocs.org/media/pdf/django-plotly-dash/latest/django-plotly-dash.pdf<br /> 

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
