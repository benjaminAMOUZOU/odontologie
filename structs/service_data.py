"""Classe singleton"""

__author__ = "Jean-Claude OFFRIDAM"
__createAt__ = "09/02/2022"
__updateAt__ = "09/02/2022"

from structs.read import Serialize
from configs import base
from untils import file
import json

serialize = Serialize()

class ServiceData:
    __instance = None

    @staticmethod
    def get_instance():
        if ServiceData.__instance == None:
            ServiceData.__instance = ServiceData()
        return ServiceData.__instance

    def __init__(self):
        self.MALADIES = serialize.get_maladies()
        self.PATIENTS = serialize.get_patients()
        self.CONSULTATIONS = serialize.get_consultations()
        self.TYPE_CONSULTATIONS = serialize.get_type_consultations()
        self.SYMPTOMES = serialize.get_symptomes()
        self.TRAITEMENTS = serialize.get_traitements()
        self.PRATICIENS = serialize.get_praticiens()
        self.CONSULTATION_MALADIES = serialize.get_consultation_maladie()

    def get_element(self, id, elements):
        for item in elements:
            if item.id == id:
                return item
        return None

    def get_elements(self, ids, elements):
        results = []
        for id in ids:
            item = self.get_element(id, elements)
            if item != None:
                results.append(item)
        return results

    def foreign_elements(self, id, foreign_id, elements):
        results = []
        for item in elements:
            if item.__dict__[foreign_id] == id:
                results.append(item)
            return results

    def deserialize(self):
        json_data = {
            "praticiens":[],
            "patients":[],
            "maladies":[],
            "traitements":[],
            "symptomes":[],
            "consultations_type":[],
            "consultations":[],
            "consultation_maladie":[]
        }

        for item in self.MALADIES:
            json_data["maladies"].append(json.loads(item.to_json()))
        for item in self.PATIENTS:
            json_data["patients"].append(json.loads(item.to_json()))
        for item in self.CONSULTATIONS:
            json_data["consultations"].append(json.loads(item.to_json()))
        for item in self.TYPE_CONSULTATIONS:
            json_data["consultations_type"].append(json.loads(item.to_json()))
        for item in self.SYMPTOMES:
            json_data["symptomes"].append(json.loads(item.to_json()))
        for item in self.TRAITEMENTS:
            json_data["traitements"].append(json.loads(item.to_json()))
        for item in self.PRATICIENS:
            json_data["praticiens"].append(json.loads(item.to_json()))
        for item in self.CONSULTATION_MALADIES:
            json_data["consultation_maladie"].append(json.loads(item.to_json()))

        with open(base.FILE, 'w') as file:
            file.write(json.dumps(json_data, indent=4))


    def deserialize_output(self):
        json_data = {
            "patients":[]
        }

        for patient_item in self.PATIENTS:

            patient = {
                "id": patient_item.id,
                "nom": patient_item.nom,
                "prenom": patient_item.prenom,
                "sexe": patient_item.sexe,
                "date_naissance": patient_item.date_naissance,
                "group_sanguin": patient_item.group_sanguin,
                "consultations": [],
                "created_at": patient_item.created_at,
                "updated_at": patient_item.updated_at
            }

            consultations_patient = self.get_elements(patient_item.consultations, self.CONSULTATIONS)
            for consultation_item in consultations_patient:
                type = self.get_element(consultation_item.type_id, self.TYPE_CONSULTATIONS)
                consultations = {
                    "id": consultation_item.id,
                    "type": type.libelle if type != None else None,
                    "observation": consultation_item.observation,
                    "created_at": consultation_item.created_at,
                    "updated_at": consultation_item.updated_at,
                    "maladies": [],
                    "symptomes": []
                }

                symptomes_consultation = self.get_elements(consultation_item.symptomes, self.SYMPTOMES)
                for symptome_item in symptomes_consultation:
                    symptome = {
                        "id": symptome_item.id,
                        "libelle": symptome_item.libelle,
                        "description": symptome_item.description,
                        "created_at": symptome_item.created_at,
                        "updated_at": symptome_item.updated_at
                    }
                    consultations['symptomes'].append(symptome)

                maladies_consultation = self.foreign_elements(consultation_item.id, 'consultation_id', self.CONSULTATION_MALADIES)
                for maladie_item in maladies_consultation:
                    __maladie = self.get_element(maladie_item.maladie_id, self.MALADIES)
                    maladie = {
                        "id": __maladie.id,
                        "libelle": __maladie.libelle,
                        "description": __maladie.description,
                        "debut_traitement": maladie_item.debut_traitement,
                        "fin_traitement": maladie_item.fin_traitement,
                        "traitement_reussi": maladie_item.traitement_reussi,
                        "created_at": __maladie.created_at,
                        "updated_at": __maladie.updated_at
                    }
                    consultations['maladies'].append(maladie)
                patient['consultations'].append(consultations)
            json_data['patients'].append(patient)

        with open(base.OUTPUT_FILE, 'w') as file:
            file.write(json.dumps(json_data, indent=4))
