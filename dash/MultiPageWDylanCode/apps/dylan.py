import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import server

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

layout = html.Div(children=[
    html.H3('You are viewing information on {}'.format(dcc.Location)),

    #Header
    html.H1(children='QC Benchmarker', className = "app-header"),
    
    #### insert link code
    dcc.Location(id='url', refresh=False),

    # content will be rendered in this element
    html.Div(id='page-content'),
    #### end of insert
    
    #main Row div
    html.Div([
        html.Div(#Column 1: Sample
            [
                html.H5(children='Sample'),
                html.P(children='Status Information'),
                html.A([ # Clickable image that links you to a page defined at the bottom
                   html.Img(src="images/greenbox.png")],href='/sample'),
            ],
            className="col-sm" # "" or maybe column?
        ),#Column 2: LC
        html.Div(
            [
                html.H5(children='LC'),
                html.P(children='General Information'),
                html.A([ # Clickable image
                   html.Img(src="a.png")],href='/dylan/lc'),
            ],
            className="col-sm"
        ),#Column 3: Source
        html.Div(
            [
                html.H5(children='Source'),
                html.P(children='Information'),
                html.A([ # Clickable image
                   html.Img(src="a.png")],href='/dylan/source'),
            ],
            className="col-sm"
        ),#Column 6: MS1
        html.Div(
            [
                html.H5(children='MS1'),
                html.P(children='Information'),
                html.A([ # Clickable image
                   html.Img(src="a.png")],href='/dylan/ms1'),
            ],
            className="col-sm"
        ),#Column 5: MS2
        html.Div(
            [
                html.H5(children='MS2'),
                html.P(children='Information'),
                html.A([ # Clickable image
                   html.Img(src="a.png")],href='/dylan/ms2'),
            ],
            className="col-sm"
        ),
    ],
    #End of row
    className="row"
),
])

#### rest of link code
def display_page(pathname):
   if (pathname != '/dylan'):#'/page-2'):
      return html.Div([
         html.H3('You are viewing information on {}'.format(pathname))
      ])
