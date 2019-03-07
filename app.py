# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from pyteomics import fasta



app = dash.Dash(__name__)

app.layout = html.Div(children=[
	#QC BENCHMARKER HEADER
    html.H1(children='QC Benchmarker', className = "app-header"),
	#BEGIN DROP DOWN MENU
	dcc.Dropdown(
	#BEGIN OPTIONS
	options=[
        {'label': 'Hela', 'value': 'HELA'},
        {'label': 'neeley', 'value': 'NEELEY'}
    ],
	#END OPTIONS
    value='OPT'
	),
	#END DROP DOWN
	#START UPLOAD CODE
	dcc.Upload(
        id='upload-data',
		#BEGIN INSIDE BOX TEXT
        children=html.Div([
				html.Div('Drag and Drop or ', style={'text-align':'center', 'vertical-align': 'middle', 'line-height': '500px'}),
				#END INNER DIV
				 html.A('Select Files',className="app-typography--a"),
				 #END HTML A
		], #END DIV,
		#END INSIDE BOX TEXT

		#BEGIN STYLE OF BOX AROUND UPLOAD
        style={
			'margin': 'auto',
			'width': '50%',
            'height': '500px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',


        },
		#END STYLE OF BOX AROUND UPLOAD

    ),
	#END OUTTER DIV
),
# END UPLOAD
	html.Div(id='output-data-upload'),

])
#end app.layout
##############################################################################################################################


if __name__ == '__main__':
    app.run_server(debug=True)
