import dash
import dash_html_components as html
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import subprocess
import string
import random

#https://community.plot.ly/t/dash-upload-component-decoding-large-files/8033/10
#also utilizes proteowizard's msconvert http://proteowizard.sourceforge.net/download.html
#http://flask.pocoo.org/docs/1.0/patterns/fileuploads/

cwd = os.getcwd()
UPLOAD_FOLDER = "/project/app_uploaded_files"
ALLOWED_EXTENSIONS = set(['raw', 'fasta'])

#YOUR INSTALLATION PATH TO MSCONVERT WILL VARY
#msconvert = "C:/Program Files/ProteoWizard/ProteoWizard 3.0.19073.85be84641/msconvert.exe"
msconvert = "C:/Program Files/ProteoWizard/ProteoWizard 3.0.19082.ade61137d/msconvert.exe"

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div( 
        children=[
            html.Iframe(id='iframe-upload',src=str.format('/upload')),
            html.Div(id='output')
                ]
)

def IDgen():
    idlen = 10
    collisions = 0
    ID = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(idlen)) #generate ID
    while os.path.exists(UPLOAD_FOLDER + "/" + str(ID)):
        collisions += 1
        if collisions >= 10:
            collisions = 0
            idlen = idlen + 1
        ID = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(idlen)) #generate new ID
    print(ID)
    return str(ID)

def DIRgen(ID):
    print(ID)
    DIR = UPLOAD_FOLDER + "/" + ID
    os.mkdir(DIR)
    print(DIR)
    return DIR

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.server.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if not os.path.exists(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)

        if file and allowed_file(file.filename):
            mspath = DIRgen(IDgen())
            file.save(mspath+"/"+filename)

            if filename.rsplit('.', 1)[1].lower() == "raw":
                cmd = msconvert + " " + mspath +"/" +filename + " -o " + mspath
                subprocess.run(cmd)
                
            print("Done: " + mspath)
        else:
            print("Invalid Input")

    return '''
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
if __name__ == '__main__':
   app.run_server(debug=True)