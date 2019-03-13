https://dash.plot.ly/urls

dylancode is taken from dylan's branch, just to try to get a nice multi-user demo going

Here's how to structure a multi-page app, where each app is contained in a separate file.
File structure:
- app.py
- index.py
- apps
   |-- __init__.py
   |-- app1.py
   |-- app2.py

Each app runs independently, and resets if you leave
Run from index.py
current urls are 
   http://127.0.0.1:8050/app1
   http://127.0.0.1:8050/dylan
   
dylan url also has suburls, reachable by clicking the images
