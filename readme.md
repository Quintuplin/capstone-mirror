This is a Django application with a dash app embedded inside it. 
1. Activate the virtual environment 
> source myenv/bin/activate
2. cd into capstone directory 
3. run the server 
> python3 manage.py runserver <br /> 
------------------------------------------------------------------------------- <br />

* uploads go into the uploads directory with a custom URL <br />
* capstone directory controls all of the URL <br /> 
* dash_results directory is the dash app <br /> 
* upload directoy is the django upload app that links to the dash app <br />
* manage.py is how django controls everything- migrating, running the server, making apps etc. 
