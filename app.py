# front of app- just setting up with no page
import dash
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

from flask import Flask
import flask
server = flask.Flask(__name__)
app = dash.Dash(__name__,external_stylesheets=external_stylesheets, server=server, static_folder ='static')

app.config.suppress_callback_exceptions = True
