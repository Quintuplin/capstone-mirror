# Final Stretch

## Saves to uploads folder, which is now just outside the django app but still within the github sync

### Note: env should not be synced because there are some OS-specific (and potentially user-specific) quirks. It's much safer to simply make your own venv env (or venv myenv if you so prefer) and not sync it.<br /> 

## To run the app django-style
0. Ensure that you have installed and are using python 3.6.8

Linux Instructions
1. Setup the virtual environment <br /> 
python3 -m venv env / python3 -m venv myenv
2. Activate the virtual environment <br /> 
source env/bin/activate / source myenv/bin/activate 
3. Install dependencies<br /> 
pip install -r requirements.txt<br /> 
4. Move the terminal to the capstone directory<br />
cd capstone
5. run the server <br /> 
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
4. Move the terminal to the capstone directory<br />
cd capstone
5. run the server <br /> 
python3 manage.py migrate <br /> 
python3 manage.py runserver <br /> 

------------------------------------------------------------------------------- <br />

* uploads go into the uploads directory with a custom URL <br />
* capstone directory controls all of the URL <br /> 
* dash_results directory is the dash app <br /> 
* upload directoy is the django upload app that links to the dash app <br />
* manage.py is how django controls everything- migrating, running the server, making apps etc. <br /> 
