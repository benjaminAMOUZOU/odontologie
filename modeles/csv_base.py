from untils.date import nowtostr
import json

class CsvBase:
    def __init__(self, date_consultation, type_consulation, nom, prenom, date_naissance, sexe, groupe_sanguin, symptomes, maladie, traite, date_fin_traitement, praticien, observation, date_premiere_consultation) -> None:
        self.date_consultation = date_consultation
        self.type_consulation = type_consulation
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.groupe_sanguin = groupe_sanguin
        self.symptomes = symptomes
        self.maladie = maladie
        self.traite = traite
        self.date_fin_traitement = date_fin_traitement
        self.praticien = praticien
        self.observation = observation
        self.date_premiere_consultation = date_premiere_consultation

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)
