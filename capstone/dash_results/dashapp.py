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

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=query_df['Time'],
                    y=query_df['TIC'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name= 'query'
                ),
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
                )
            ],
            'layout': go.Layout(
                xaxis={'type': 'log',
                       'title': 'Time'},
                yaxis={'type': 'log',
                       'title': 'TIC'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])
