# -*- coding: utf-8 -*-
"""Point pour l'interface web"""

__author__ = "Benjamin AMOUZOU"
__createAt__ = "02/03/2022"
__updateAt__ = "02/03/2022"

import os
from flask import Flask, render_template, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename
#from flask.ext.session import Session

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}

app=Flask(__name__, template_folder="templates")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#sess = Session()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/')
def home():
    return render_template('index.html')

if __name__=="__main__":
    app.secret_key = 'clé secrete'
    app.config['SESSION_TYPE'] = 'filesystem'
    #sess.init_app(app)
    app.debug = True
    app.run(debug=True)