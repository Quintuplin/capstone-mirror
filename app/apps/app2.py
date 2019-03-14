# -*- coding: utf-8 -*-
#Pipeline output page
import dash
import dash_core_components as dcc
import dash_html_components as html
#import dash_bootstrap_components
from app import app

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# using local version for local testing straight from
#       https://codepen.io/chriddyp/pen/bWLwgP.css
#external_stylesheets = ['bWLwgP_chriddyp_codepen.css']#static/css/

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

layout = html.Div(children=[
    #Header
    html.H1(children='QC Benchmarker', className = "app-header"),
    
    #### insert link code
    #dcc.Location(id='url', refresh=False),

    # content will be rendered in this element
    html.Div(id='pipe-content'),
    #### end of insert
    
    #main Row div
    
])

#### rest of link code
@app.callback(dash.dependencies.Output('pipe-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_value(pathname):#was diplay_page
   if (pathname != '/apps/app2'):
      return html.Div([#
         html.H3('You are viewing information on {}'.format(pathname))
      ])
   else:
        return html.Div([
        html.Div(#Column 1: Sample
            [
                html.H5(children='Sample'),
                html.P(children='Status Information'),
                html.A([ # Clickable image that links you to a page defined at the bottom
                   html.Img(src="images/greenbox.png")],href='app2/sample'),
            ],
            className="col-sm" # "" or maybe column?
        ),#Column 2: LC
        html.Div(
            [
                html.H5(children='LC'),
                html.P(children='General Information'),
                html.A([ # Clickable image
                   html.Img(src="a.png")],href='app2/lc'),
            ],
            className="col-sm"
        ),#Column 3: Source
        html.Div(
            [
                html.H5(children='Source'),
                html.P(children='Information'),
                html.A([ # Clickable image
                   html.Img(src="a.png")],href='app2/source'),
            ],
            className="col-sm"
        ),#Column 6: MS1
        html.Div(
            [
                html.H5(children='MS1'),
                html.P(children='Information'),
                html.A([ # Clickable image
                   html.Img(src="a.png")],href='app2/ms1'),
            ],
            className="col-sm"
        ),#Column 5: MS2
        html.Div(
            [
                html.H5(children='MS2'),
                html.P(children='Information'),
                html.A([ # Clickable image
                   html.Img(src="a.png")],href='app2/ms2'),
            ],
            className="col-sm"
        ),
    ],
    #End of row
    className="row")
#### end of rest

if __name__ == '__main__':
    app.run_server(debug=True)
