from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html


import plotly.plotly as py
import dash
import plotly.graph_objs as go
import os

import numpy as np
import pandas as pd
from .server import app
from . import router

from .layouts  import layout1, box_results

# change your directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

query_file = BASE_DIR + '/que.csv'
reference_file = BASE_DIR + '/ref.csv'

query_df = pd.read_csv(query_file)

reference_df = pd.read_csv(reference_file)




colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.index_string = '''
<!DOCTYPE html>
<html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">



<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

<style type="text/css">
			html, body {
					height: 100%;
					margin: 0;
			}

			#wrapper {
					min-height: 100%;
			}
			#uploadbox{
				background-color: lightgrey;
				margin:25px auto;
				width: 50%;
				text-align: center;
				border: dotted;
				padding: 25px;


			}
		#submitButton{
    height:50px;
    width:100px;
    margin: 25px auto;
    bottom: 10px;

}
	</style>

</head>
<!----------------------------------------------------------------------------------------------------------------------------------------->

<nav class="navbar sticky-top navbar-light bg-color" style="background-color: #659EC7;">

	

			<button class="navbar-toggler"
							type="button"
							data-toggle="collapse"
							data-target="#navbarNav"
							aria-controls="navbarNav"
							aria-expanded="false"
							aria-label="Toggle navigation">

				<span class="navbar-toggler-icon"></span>

			</button>

		  <div class="collapse navbar-collapse" id="navbarNav">
		    <ul class="navbar-nav">
		      <li class="nav-item active">
		        <a class="nav-link" href="{%url 'home'%}">Home <span class="sr-only">(current)</span></a>
		      </li>
		      <li class="nav-item">
		        <a class="nav-link" href="{%url 'about'%}">About</a>
		      </li>
		      <li class="nav-item">
		        <a class="nav-link" href="{%url 'contact'%}">Contact</a>
		      </li>

		    </ul>
		  </div>
</nav>
<body>
    <div id="wrapper">

		{%app_entry%}
	</div>
	  {%config%}
            {%scripts%}
            {%renderer%}
</body>

</html>



'''



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):

    if pathname  == '/dash_results/':
        return box_results
    elif pathname == '/dash_results/result_one/':
        return layout1
    else:
        return '404'



