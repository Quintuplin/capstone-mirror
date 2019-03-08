# -*- coding: utf-8 -*-
# Pipeline output page with 
import dash
import dash_core_components as dcc
import dash_html_components as html
#import dash_bootstrap_components
#need to make sure css is working
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
    #Header
    html.H1(children='QC Benchmarker', className = "app-header"),
    #main Row div
    html.Div([
        html.Div(#Column 1: Sample
            [
                html.H5(children='Sample'),
                html.P(children='Status Information'),
                html.Img(src="a.png"),
            ],
            className='col-sm' # "" or maybe column?
        ),#Column 2: LC
        html.Div(
            [
                html.H5(children='LC'),
                html.P(children='General Information'),
                html.Img(src="a.png"),
            ],
            className="col-sm"
        ),#Column 3: Source
        html.Div(
            [
                html.H5(children='Source'),
                html.P(children='Information'),
                html.Img(src="a.png"),
            ],
            className="col-sm"
        ),#Column 6: MS1
        html.Div(
            [
                html.H5(children='MS1'),
                html.P(children='Information'),
                html.Img(src="a.png"),
            ],
            className="col-sm"
        ),#Column 5: MS2
        html.Div(
            [
                html.H5(children='MS2'),
                html.P(children='Information'),
                html.Img(src="a.png"),
            ],
            className="col-sm"
        ),
    ],
    #End of row
    className="row"
),
])

if __name__ == '__main__':
    app.run_server(debug=True)

