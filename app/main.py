import os
# instance of flask class will be our WSGI application

import dash_core_components as dcc
import dash_html_components as html
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory
from app import app

# store files uploaded in the /uploads directory
UPLOAD_FOLDER = '/home/misae/Documents/uploads'
# we are allowing raw and fasta files
# important so users cannot upload odd files like HTML files that would cause XSS problems
ALLOWED_EXTENSIONS = {'raw', 'fasta'}

# instnce of Flask class
# _name_ is needed to tell flask where to look for tempmlates
#app1 = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#layout = index.html
#up_layout = index.html

@app.server.route('/')
def index():
    return render_template('index.html')

def upload_layout():
    return index #'index.html'
#dash version of index.html
layout = html.Div(
    [
        html.H1('Upload new File'),
        html.Form(
            [
                dcc.Input(id = 'filename',type='file',name='file'),
                dcc.Input(id = 'submitload',type='submit',value='Upload'),
            ],
            method='post',#enctype='multipart/form-data',
        ),
    ],
),



# this method was provided in the flask documentation
# purpose: checks to see if the file is allowed to be uploaded based on our ALLOWED_EXTENSIONS var
# attribution: http://flask.pocoo.org/docs/1.0/patterns/fileuploads/
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# app.route tells flask what URL should trigger upload_file()
@app.server.route('/', methods=['GET', 'POST'])
# this method was provided in the flask doccumentation
# purpose: uploads file and redirects user to the url of that file
# attribution: http://flask.pocoo.org/docs/1.0/patterns/fileuploads/
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index',
                                    filename=filename))

        return redirect(url_for('index'))


# tells flask /uploads/filename url should trigger uploaded_file()

@app.server.route('/uploads/<filename>')
# this method was provided in the flask documentaiton
# purpose: serves user the uploaded files
# attribution: http://flask.pocoo.org/docs/1.0/patterns/fileuploads/
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
if __name__ == "__main__":
    # Only for debugging while developing
    app.run(debug=True)#run(host='0.0.0.0', debug=True, port=80)
