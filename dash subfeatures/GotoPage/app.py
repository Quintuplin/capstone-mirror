import dash
import dash_html_components as html
import dash_core_components as dcc
from flask import Flask, redirect

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Location(id='url', refresh=True),

    html.Div(dcc.Input(id='input-box', type='text')),
    html.Button('Submit', id='button'),
    html.Div(id='output-container-button',
             children='Enter a value and press submit')
])

@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('url', 'pathname')],
    [dash.dependencies.State('input-box', 'value')])
def update_output(pathname, value):
    redirect('/' + str(value))
    return 'The input value was "{}"'.format(
        value
    )

if __name__ == '__main__':
    app.run_server(debug=True)