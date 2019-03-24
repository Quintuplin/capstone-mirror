import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app1, dylan


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    #html.H3('You are viewing information on {}'.format(pathname)),
    if pathname == '/app1':
        return app1.layout
    elif "/dylan" in str(pathname):
        return dylan.layout
    else:
        return app1.layout

if __name__ == '__main__':
    app.run_server(debug=True)