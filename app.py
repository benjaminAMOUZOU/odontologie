# -*- coding: utf-8 -*-
"""Point d'entrée pour l'interface web"""

__author__ = "Benjamin AMOUZOU"
__createAt__ = "02/03/2022"
__updateAt__ = "02/03/2022"

import os
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from flask_session import Session
from structs.service_data import ServiceData
from structs.csv_parser import CsvParser

#Répertoire contenant le fichier et l'extension autorisé
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}

app=Flask(__name__, template_folder="templates")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
sess = Session()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        #Vérification du name de l'input
        if 'file' not in request.files:
            erreur = "Vous n'avez pas sélectionner un fichier !"
            return render_template('index.html', erreur=erreur)

        file = request.files['file']

        #Vérification de l'envoi d'un fichier
        if request.files['file'].filename == '':
            erreur = "Vous n'avez pas sélectionner un fichier !"
            return render_template('index.html', erreur=erreur)

        #Vérification du fichier et de l'extension
        if file and allowed_file(file.filename):
            service = ServiceData.get_instance()
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            #Traitement sur le fichier
            cp = CsvParser("uploads/{}".format(filename))
            cp.run()

            service.deserialize()
            service.deserialize_output()
            message="Le traitement a été effectué avec succès sur " + filename + " !"
            return render_template('index.html', message=message)
        else:
            erreur = "L'extension de " + request.files['file'].filename + " n'est pas du csv !"
            return render_template('index.html', erreur=erreur)
    else:
        erreur = "Vous n'êtes pas autorisé !"
        return render_template('index.html', erreur=erreur)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/data')
def data():
    service = ServiceData.get_instance()
    return render_template('data.html', consultations=service.CONSULTATIONS)

if __name__=="__main__":
    app.secret_key = 'clé secrete'
    app.config['SESSION_TYPE'] = 'filesystem'
    sess.init_app(app)
    app.debug = True
    app.run(debug=True)