"""Classe singleton"""

__author__ = "Jean-Claude OFFRIDAM"
__createAt__ = "09/02/2022"
__updateAt__ = "09/02/2022"

from structs.read import Serialize
from configs import base
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
