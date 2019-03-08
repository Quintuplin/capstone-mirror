https://dash.plot.ly/urls

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
working url is http://127.0.0.1:8050/apps/app1
   (plain url returns 404)