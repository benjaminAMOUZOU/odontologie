import os
import json
from configs import base
from modeles import *

class Serialize:
    def __init__(self):
        self.json_data = self.load_file()

    def check_file_exit(self, path=base.FILE) -> bool:
        if os.path.exists(path):
            return True
        return False

    def check_file_empty(self, path=base.FILE) -> bool:
        if os.path.getsize(path) <= 0:
            return True
        return False

    def init_file(self, path=base.FILE, struct=base.BASE_STRUCT):
        with open(path, 'w') as file:
            json.dump(struct, file)

    def create_file(self, path=base.FILE, struct=base.BASE_STRUCT):
        if not self.check_file_exit(path) or self.check_file_empty(path):
            self.init_file(path, struct)

    def load_file(self, path=base.FILE):
        self.create_file()
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
            data = Patient(item['id'], item['nom'], item['prenom'], item['sexe'], item['date_naissance'], item['groupSanguin'], item['created_at'], item['updated_at'])
            elements.append(data)
        return elements

    def get_maladies(self):
        elements_data = self.json_data['maladies']
        elements = list()
        for item in elements_data:
            data = Maladie(item['id'], item['libelle'], item['description'], item['created_at'], item['updated_at'])
            elements.append(data)
        return elements

    def get_traitements(self):
        elements_data = self.json_data['traitements']
        elements = list()
        for item in elements_data:
            data = Traitement(item['id'], item['libelle'], item['description'], item['created_at'], item['updated_at'])
            elements.append(data)
        return elements

    def get_symptomes(self):
        elements_data = self.json_data['symptomes']
        elements = list()
        for item in elements_data:
            data = Symptome(item['id'], item['libelle'], item['description'], item['created_at'], item['updated_at'])
            elements.append(data)
        return elements

    def get_type_consultations(self):
        elements_data = self.json_data['consultations_type']
        elements = list()
        for item in elements_data:
            data = TypeConsultation(item['id'], item['libelle'], item['created_at'], item['updated_at'])
            elements.append(data)
        return elements

    def get_consultations(self):
        elements_data = self.json_data['consultations']
        elements = list()
        for item in elements_data:
            data = Consultation(item['id'], item['observation'], item['created_at'], item['updated_at'])
            elements.append(data)
        return elements

    def get_consultation_maladie(self):
        elements_data = self.json_data['consultation_maladie']
        elements = list()
        for item in elements_data:
            data = ConsultationMaladie(item['id'], item['debut_traitement'], item['fin_traitement'], item['traitement_reussi'], item['created_at'], item['updated_at'])
            elements.append(data)
        return elements


class Deserialize:
    def __init__(self):
        pass