# front of app- just setting up with no page
import dash
import dash_core_components as dcc
import dash_html_components as html
from flask import Flask, flash, request, redirect, url_for, render_template

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# Made the flask app the dash server
server = Flask(__name__)
app = dash.Dash(__name__,server=server,external_stylesheets=external_stylesheets)
#server = app.server
app.config.suppress_callback_exceptions = True
