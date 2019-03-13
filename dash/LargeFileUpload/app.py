from os.path import join
from flask import Flask, flash, request
from werkzeug.utils import secure_filename
import dash
import dash_html_components as html
import os
cwd = os.getcwd()
UPLOAD_FOLDER = "/project/app_uploaded_files"

#https://community.plot.ly/t/dash-upload-component-decoding-large-files/8033/10
#tos:https://community.plot.ly/tos
#relevant CC license details for community content: https://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US
#takeaway: attribution, non-commercial, share-alike

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.layout = html.Div( 
        children=[
            #html.Iframe(id='iframe-upload',src=f'/upload'),
            html.Iframe(id='iframe-upload',src=str.format('/upload')),
            html.Div(id='output')
                ]
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


    return '''
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
if __name__ == '__main__':
   app.run_server(debug=True)