from flask import Flask, flash, request
from werkzeug.utils import secure_filename
from urllib.parse import quote as urlquote

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import os
from os.path import join
import subprocess
cwd = os.getcwd()

#attempting to combine smconvert with file management
#no crash, but non-functional
#utilize app.py not this one

#https://community.plot.ly/t/dash-upload-component-decoding-large-files/8033/10
#tos:https://community.plot.ly/tos
#relevant CC license details for community content: https://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US
#takeaway: attribution, non-commercial, share-alike
#https://docs.faculty.ai/user-guide/apps/examples/dash_file_upload_download.html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

UPLOAD_FOLDER = "/project/app_uploaded_files"
msconvert = "C:/Program Files/ProteoWizard/ProteoWizard 3.0.19073.85be84641/msconvert.exe"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.layout = html.Div( 
    [
        html.H1("File Browser"),
        html.H2("Upload"),
        #html.Iframe(id='iframe-upload',src=f'/upload'),
        html.Iframe(id='iframe-upload',src=str.format('/upload')),
        html.Div(id='output'),
        html.H2("File List"),
        html.Ul(id="file-list"),
    ],
    style={"max-width": "500px"},
)

@app.server.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if not os.path.exists(UPLOAD_FOLDER):
      os.makedirs(UPLOAD_FOLDER)
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        #if file.exists (filename.split('.')[0]+"1." +filename.split('.')[1])
        while os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
            filename = filename.split('.')[0]+"1." +filename.split('.')[1]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        cmd = msconvert + " " + os.path.join(app.config['UPLOAD_FOLDER'], filename) + " -o " + UPLOAD_FOLDER
        subprocess.run(cmd)


    return '''
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

def uploaded_files():
    """List the files in the upload directory."""
    files = []
    for filename in os.listdir(UPLOAD_FOLDER):
        path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.isfile(path):
            files.append(filename)
    return files

def file_download_link(filename):
    """Create a Plotly Dash 'A' element that downloads a file from the app."""
    location = "/download/{}".format(urlquote(filename))
    return html.A(filename, href=location)

@app.callback(
    Output("file-list", "children"),
)
def update_output(uploaded_filenames, uploaded_file_contents):
    files = uploaded_files()
    if len(files) == 0:
        return [html.Li("No files yet!")]
    else:
        return [html.Li(file_download_link(filename)) for filename in files]

if __name__ == '__main__':
   app.run_server(debug=True)