#imports some more tools that can be passed down
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app1, pipeapp

#makes layout for app1 and pipeapp
#id 'url' used especially in pipeline
app.layout=html.Div([dcc.Location(id='url',refresh=False), 
		html.Div(id='page-content')]) #contecnt decided by url


@app.callback(Output('page-content','children'),
		[Input('url','pathname')])
#decides which app to use depending on path
def display_page(pathname):
	if pathname=='/apps/app1':
		return app1.layout
	elif pathname == '/apps/app2':
		return app2.layout
	#for now this is fine but needs to be specific to those 5 pages on pipeapp
	else:#if pathname.startswith('/apps/'):
		return app2.layout
	#else: 
		#return 'Page doesn't exist'
if __name__=='__main__':
	app.run_server(debug=True)
