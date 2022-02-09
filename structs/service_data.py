"""Classe singleton"""

__author__ = "Jean-Claude OFFRIDAM"
__createAt__ = "09/02/2022"
__updateAt__ = "09/02/2022"

from structs.read import Serialize
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