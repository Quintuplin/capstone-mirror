# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from pyteomics import fasta



app = dash.Dash(__name__)

app.layout = html.Div(children=[
	#QC BENCHMARKER HEADER
    html.H1(children='QC Benchmarker'),
	#PROVIDED BY NIST TEXT
	html.Div(children='Provided by NIST', className="app-header--title"),
	#START UPLOAD CODE
	dcc.Upload(
        id='upload-data',
		#BEGIN INSIDE BOX TEXT
        children=html.Div(['Drag and Drop or ', html.A('Select Files',className="app-typography--a")]),
		#END INSIDE BOX TEXT, GRABBING 'A' DESIGN FROM TOPOGRAPHY.CSS
		#BEGIN STYLE OF BOX AROUND UPLOAD
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
		#END STYLE OF BOX AROUND UPLOAD

    ),
	# END UPLOAD
    html.Div(id='output-data-upload'),
])
#end app.layout
##############################################################################################################################


if __name__ == '__main__':
    app.run_server(debug=True)
