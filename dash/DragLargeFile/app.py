import base64
import os
from os.path import join

from flask import Flask, flash, request, send_from_directory

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

from werkzeug.utils import secure_filename
from urllib.parse import quote as urlquote

#https://community.plot.ly/t/dash-upload-component-decoding-large-files/8033/10
#tos:https://community.plot.ly/tos
#relevant CC license details for community content: https://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US
#takeaway: attribution, non-commercial, share-alike

#https://docs.faculty.ai/user-guide/apps/examples/dash_file_upload_download.html
#also has drag and drop

cwd = os.getcwd()
UPLOAD_FOLDER = "/project/app_uploaded_files"

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.layout = html.Div( 
        children=[
            html.Iframe(id='iframe-upload',src=f'/upload'),
            html.Div(id='output')
                ],
        style={
                "width": "100%",
                "height": "60px",
                "lineHeight": "60px",
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "5px",
                "textAlign": "center",
                "margin": "10px",
            },
)

@app.server.route('/upload', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        while os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
            filename = filename.split('.')[0]+"1." +filename.split('.')[1]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return '''
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
if __name__ == '__main__':
   app.run_server(debug=True)