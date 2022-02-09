import json
from configs import base
from untils import file
from modeles import *


class Serialize:
    def __init__(self):
        self.json_data = self.load_file()

    def load_file(self, path=base.FILE, struct=base.BASE_STRUCT):
        file.create_file(path=path, struct=struct)
        with open(path, 'r') as data:
            json_data = json.load(data)
        return json_data

    def get_praticiens(self):
        elements_data = self.json_data['praticiens']
        elements = list()
        for item in elements_data:
            data = Praticien(item['id'], item['nom'], item['prenom'], item['sexe'], item['email'], item['password'], item['created_at'], item['updated_at'])
            elements.append(data)
        return elements

    def get_patients(self):
        elements_data = self.json_data['patients']
        elements = list()
        for item in elements_data:
            data = Patient(item['id'], item['nom'], item['prenom'], item['sexe'], item['date_naissance'], item['group_sanguin'], item['created_at'], item['updated_at'])
            data.set_consultations(item['consultations'])
            elements.append(data)
        return elements

    def get_maladies(self):
        elements_data = self.json_data['maladies']
        elements = list()
        for item in elements_data:
            data = Maladie(item['id'], item['libelle'], item['description'], item['created_at'], item['updated_at'])
            data.set_simptomes(item['symptomes'])
            data.set_traitements(item['traitements'])
            elements.append(data)
        return elements

    def get_traitements(self):
        elements_data = self.json_data['traitements']
        elements = list()
        for item in elements_data:
            data = Traitement(item['id'], item['libelle'], item['description'], item['created_at'], item['updated_at'])
            data.set_maladies(item['maladies'])
            elements.append(data)
        return elements

    def get_symptomes(self):
        elements_data = self.json_data['symptomes']
        elements = list()
        for item in elements_data:
            data = Symptome(item['id'], item['libelle'], item['description'], item['created_at'], item['updated_at'])
            data.set_maladies(item['maladies'])
            elements.append(data)
        return elements

    def get_type_consultations(self):
        elements_data = self.json_data['consultations_type']
        elements = list()
        for item in elements_data:
            data = TypeConsultation(item['id'], item['libelle'], item['created_at'], item['updated_at'])
            data.set_consultations(item['consultations'])
            elements.append(data)
        return elements

    def get_consultations(self):
        elements_data = self.json_data['consultations']
        elements = list()
        for item in elements_data:
            data = Consultation(item['id'], item['observation'], item['created_at'], item['updated_at'])
            data.set_simptomes(item['symptomes'])
            data.foreign(item['type_id'], item['patient_id'], item['praticien_id'], item['precedente_id'])
            elements.append(data)
        return elements

    def get_consultation_maladie(self):
        elements_data = self.json_data['consultation_maladie']
        elements = list()
        for item in elements_data:
            data = ConsultationMaladie(item['id'], item['debut_traitement'], item['fin_traitement'], item['traitement_reussi'], item['created_at'], item['updated_at'])
            data.set_simptomes(item['symptomes'])
            data.foreign(item['consultation_id'], item['maladie_id'], item['traitement_id'])
            elements.append(data)
        return elements

class Deserialize:
    def __init__(self):
        pass