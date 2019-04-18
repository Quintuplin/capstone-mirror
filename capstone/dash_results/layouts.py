from random import randint
import dash_core_components as dcc
from dash.dependencies import Output, Input
import dash_html_components as html
from . import router
from .server import app
import plotly.graph_objs as go
from . import dashapp
import dash_table

def index():
    ''' '''
##stop light box results page
box_results = html.Div([
    html.H3('hello testing'),
    dcc.Link('Go to App 2', href='/dash_results/result_one/')])
#######################################################################################################################################
## result one page graph
layout1 = html.Div([
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
                    x = dashapp.reference_df['Time'],
                    y = dashapp.reference_df['TIC'],
                    mode='lines',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name='reference'
                ),
                go.Scatter(
                    x=dashapp.query_df['Time'],
                    y=dashapp.query_df['TIC'],
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
                columns=[{"name": i, "id": i} for i in dashapp.query_df.columns],
                data=dashapp.query_df.to_dict("rows")
            )

    ],
        className='six columns'),

        html.Div([
            html.H3('REFERENCE CSV'),
            dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i} for i in dashapp.reference_df.columns],
                data=dashapp.reference_df.to_dict("rows")
            )
        ]
        , className='six columns'),
    ],className="row")

    app.css.append_css({
        'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
    })


###############################################################################################################################
#layout2 =