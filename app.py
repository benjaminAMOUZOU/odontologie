# -*- coding: utf-8 -*-
"""Point d'entrée pour l'interface web"""

__author__ = "Benjamin AMOUZOU"
__createAt__ = "02/03/2022"
__updateAt__ = "02/03/2022"

import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
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
            flash("Vous n'avez pas sélectionner un fichier !", category="error")
            return redirect(url_for("home"))

        file = request.files['file']

        #Vérification de l'envoi d'un fichier
        if request.files['file'].filename == '':
            flash("Vous n'avez pas sélectionner un fichier !", category="error")
            return redirect(url_for("home"))

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
            flash("Le traitement a été effectué avec succès sur " + filename + " !", category="message")
            return redirect(url_for("home"))
        else:
            flash("L'extension de " + request.files['file'].filename + " n'est pas du csv !", category="error")
            return redirect(url_for("home"))
    else:
        flash("Vous n'êtes pas autorisé !", category="error")
        return redirect(url_for("home"))

@app.route('/')
def home():
    service = ServiceData.get_instance()
    data = service.deserialize_output(output="JSON")
    return render_template('index.html',data=data)

def get(id, elements):
    for item in elements:
        if int(item['id']) == int(id):
            print(item)
            return item
    return None

@app.route('/detail/<id>')
def detail(id):
    service = ServiceData.get_instance()
    json_object = service.deserialize_output(output="JSON")
    data = get(id, json_object['patients'])
    print(data)
    if data == None:
        return redirect(url_for("home"))
    return render_template('detail.html',data=data)

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/data')
def data():
    service = ServiceData.get_instance()
    return render_template('data.html', consultations=service.CONSULTATIONS)

@app.route('/consultations', methods=['GET', 'POST'])
def consultations():
    service = ServiceData.get_instance()
    data = service.json_consultations()
    types = service.json_types()
    praticiens = service.json_praticiens()
    patients = service.json_patients()
    if request.method == 'POST':
        daterange = request.form.get("daterange")
        start = daterange.split('-')[0].strip()
        end = daterange.split('-')[1].strip()
        praticien = request.form.get("praticien")
        patient = request.form.get("patient")
        tpe = request.form.get("type")

        query={"patient": patient, "praticien": praticien, "type": tpe, "start":start, "end":end}
        print(query)
        data = service.json_consultations(query)

    return render_template('consultation.html', data=data, types=types['types'], praticiens=praticiens['praticiens'], patients=patients['patients'])

if __name__=="__main__":
    app.secret_key = 'clé secrete'
    app.config['SESSION_TYPE'] = 'filesystem'
    sess.init_app(app)
    app.debug = True
    app.run(debug=True)