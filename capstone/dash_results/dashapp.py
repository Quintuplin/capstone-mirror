from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html


import plotly.plotly as py
import dash
import plotly.graph_objs as go
import os
import dash_table
import numpy as np
import pandas as pd
from .server import app
from . import router

# change your directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

query_file = BASE_DIR + '/que.csv'
reference_file = BASE_DIR + '/ref.csv'

query_df = pd.read_csv(query_file)
query_df = query_df.head(50)
print(query_df)

reference_df = pd.read_csv(reference_file)
print(reference_df)



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
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Scatter Plot', value='tab-1'),
        dcc.Tab(label='Data Table', value='tab-2'),
    ]),
    html.Div(id='tabs-content')
])
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
        dcc.Graph(
            id='total-ion',
            figure={
            'data': [
                go.Scatter(
                    x = reference_df['Time'],
                    y = reference_df['TIC'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name='reference'
                ),
                go.Scatter(
                    x=query_df['Time'],
                    y=query_df['TIC'],
                    mode='lines',
                    opacity=0.7,
                    marker={
                        'size': 13,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name= 'query'
                )
            ],
            'layout': go.Layout(
                xaxis={'type': 'linear',
                       'title': 'Retention Time (min)',
                       'titlefont' : {'size' : 18, 'color' : 'grey'},
                       'showticklabels' : True,
                       #'tickangle' : 30,
                       'tickfont' : {'size' : 14, 'color' : 'black'},
                       'gridcolor' : 'darkgrey',
                       'linecolor' : 'black',
                       'exponentformat' : 'e',
                       'showexponent' : 'all'},
                yaxis={'type': 'log',
                       'title': 'Total Ion Current',
                       'titlefont' : {'size' : 18, 'color' : 'grey'},
                       'showticklabels' : True,
                       'tickangle' : 30,
                       'tickfont' : {'size' : 14, 'color' : 'black'},
                       'dtick' : 1,
                       'gridcolor' : 'darkgrey',
                       'linecolor' : 'black',
                       'exponentformat' : 'e',
                       'showexponent' : 'all'},
                margin={'l': 80, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])
    elif tab == 'tab-2':
        return html.Div([
        html.Div([
            html.H3('QUERY CSV'),
            dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i} for i in query_df.columns],
                data=query_df.to_dict("rows")
            )

    ],
        className='six columns'),

        html.Div([
            html.H3('REFERENCE CSV'),
            dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i} for i in reference_df.columns],
                data=reference_df.to_dict("rows")
            )
        ]
        , className='six columns'),
    ],className="row")

    app.css.append_css({
        'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
    })





