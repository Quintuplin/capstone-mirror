# -*- coding: utf-8 -*-
#Pipeline output page
import dash
import dash_core_components as dcc
import dash_html_components as html
#import dash_bootstrap_components

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# using local version for local testing straight from
#       https://codepen.io/chriddyp/pen/bWLwgP.css
external_stylesheets = ['static/css/bWLwgP_chriddyp_codepen.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
    #Header
    html.H1(children='QC Benchmarker', className = "app-header"),
    
    #### insert link code
    dcc.Location(id='url', refresh=False),

    # content will be rendered in this element
    html.Div(id='page-content'),
    #### end of insert
    
])

#### rest of link code
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
   if (pathname != '/'):#'/page-2'):
      return html.Div([
         html.H3('You are viewing information on {}'.format(pathname))
      ])
	else:
		#main Row div of pipeline page
		return html.Div([
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
                   html.Img(src="a.png")],href='/lc'),
            ],
            className="col-sm"
        ),#Column 3: Source
        html.Div(
            [
                html.H5(children='Source'),
                html.P(children='Information'),
                html.A([ # Clickable image
                   html.Img(src="a.png")],href='/source'),
            ],
            className="col-sm"
        ),#Column 6: MS1
        html.Div(
            [
                html.H5(children='MS1'),
                html.P(children='Information'),
                html.A([ # Clickable image
                   html.Img(src="a.png")],href='/ms1'),
            ],
            className="col-sm"
        ),#Column 5: MS2
        html.Div(
            [
                html.H5(children='MS2'),
                html.P(children='Information'),
                html.A([ # Clickable image
                   html.Img(src="a.png")],href='/ms2'),
            ],
            className="col-sm"
        ),
    ],
    #End of row
    className="row")
#### end of rest

if __name__ == '__main__':
    app.run_server(debug=True)


