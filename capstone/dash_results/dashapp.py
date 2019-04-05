from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import dash

from .server import app
from . import router



colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
    #Header
    html.H1(children='QC Benchmarker', className = "app-header"),
	html.Div([
        html.Div(#Column 1: Sample
            [
                html.H5(children='Sample'),
                html.P(children='Status Information'),
                html.A([ # Clickable image that links you to a page defined at the bottom
                   html.Img(src="images/greenbox.png")],href='apps/sample'),
            ],
            className="col-sm" # "" or maybe column?
		),#Column 2: LC
		html.Div(
            [
                html.H5(children='LC'),
                html.P(children='General Information'),
                html.A([ # Clickable image
                   html.Img(src="a.png")],href='/apps/lc'),
            ],
            className="col-sm"
		 ),#Column 3: Source
        html.Div(
            [
                html.H5(children='Source'),
                html.P(children='Information'),
                html.A([ # Clickable image
                   html.Img(src="a.png")],href='/apps/source'),
            ],
            className="col-sm"
        ),#Column 6: MS1
        html.Div(
            [
                html.H5(children='MS1'),
                html.P(children='Information'),
                html.A([ # Clickable image
                   html.Img(src="a.png")],href='/apps/ms1'),
            ],
            className="col-sm"
        ),#Column 5: MS2
        html.Div(
            [
                html.H5(children='MS2'),
                html.P(children='Information'),
                html.A([ # Clickable image
                   html.Img(src="a.png")],href='/apps/ms2'),
            ],
            className="col-sm"
        ),
    ],
    #End of row
className="row")
    #main Row div

])#### end of layout
