"""Classe singleton"""

__author__ = "Jean-Claude OFFRIDAM"
__createAt__ = "09/02/2022"
__updateAt__ = "09/02/2022"

from structs.read import Serialize
from configs import base
from untils import file, date
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

    def get(self, value, key, elements):
        for item in elements:
            if item.__dict__[key] == value:
                return item
        return None

    def get_l(self, value, key, elements):
        results = []
        for item in elements:
            if item.__dict__[key] == value:
                results.append(item)
        return results

    def date_filter(self, value, key:str, filter:str, elements, format="%m/%d/%Y"):
        results = []
        for item in elements:
            if filter.upper() == "EQ":
                if date.strtodate(item.__dict__[key], format=format) == date.strtodate(value, format=format):
                    results.append(item)
            if filter.upper() == "GT":
                if date.strtodate(item.__dict__[key], format=format) > date.strtodate(value, format=format):
                    results.append(item)
            if filter.upper() == "GTE":
                if date.strtodate(item.__dict__[key], format=format) >= date.strtodate(value, format=format):
                    results.append(item)
            if filter.upper() == "LT":
                if date.strtodate(item.__dict__[key], format=format) <= date.strtodate(value, format=format):
                    results.append(item)
            if filter.upper() == "LTE":
                if date.strtodate(item.__dict__[key], format=format) <= date.strtodate(value, format=format):
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

    def json_types(self):
        json_data = {
            "types": []
        }

        for item in self.TYPE_CONSULTATIONS:

            data = {
                "id": item.id,
                "libelle": item.libelle,
                "created_at": item.created_at,
                "updated_at": item.updated_at
            }

            json_data['types'].append(data)

        return json_data

    def json_patients(self):
        json_data = {
            "patients": []
        }

        for item in self.PATIENTS:

            data = {
                "id": item.id,
                "nom": item.nom,
                "prenom": item.prenom,
                "sexe": item.sexe,
                "date_naissance": item.date_naissance,
                "group_sanguin": item.group_sanguin,
                "created_at": item.created_at,
                "updated_at": item.updated_at
            }

            json_data['patients'].append(data)

        return json_data

    def json_praticiens(self):
        json_data = {
            "praticiens": []
        }

        for item in self.PRATICIENS:
            data = {
                "id": item.id,
                "nom": item.nom,
                "prenom": item.prenom,
                "sexe": item.sexe,
                "email": item.email,
                "created_at": item.created_at,
                "updated_at": item.updated_at
            }

            json_data['praticiens'].append(data)

        return json_data

    def json_consultations(self, query={"patient":None, "praticien": None, "type":None, "start":None, "end":None}):
        json_data = {
            "consultations": []
        }

        consultations_data = self.CONSULTATIONS
        print(0, consultations_data)
        print(11, query['praticien'])
        if query['praticien'] != None and query['praticien'] != '0':
            consultations_data = self.get_l(int(query['praticien']), 'praticien_id', consultations_data)
            print(1,consultations_data)
        if query['praticien'] != None and query['patient'] != '0':
            consultations_data = self.get_l(int(query['patient']), 'patient_id', consultations_data)
            print(2,consultations_data)
        if query['type'] != None and query['type'] != '0':
            consultations_data = self.get_l(int(query['type']), 'type_id', consultations_data)
            print(3,consultations_data)
        if query['start'] != None:
            consultations_data = self.date_filter(query['start'], 'created_at', "gte", consultations_data)
            print(4,consultations_data)
        if query['end'] != None:
            consultations_data = self.date_filter(query['end'], 'created_at', "lte", consultations_data)
            print(5,consultations_data)

        for item in consultations_data:
            type = self.get_element(item.type_id, self.TYPE_CONSULTATIONS)
            praticien = self.get_element(item.praticien_id, self.PRATICIENS)
            patient = self.get_element(item.patient_id, self.PATIENTS)
            data = {
                "id": item.id,
                "type": type.libelle if type != None else None,
                "praticien": "{} {}".format(praticien.nom, praticien.prenom),
                "patient": "{} {}".format(patient.nom, patient.prenom),
                "observation": item.observation,
                "created_at": item.created_at,
                "updated_at": item.updated_at,
                "maladies": [],
                "symptomes": []
            }

            symptomes_consultation = self.get_elements(item.symptomes, self.SYMPTOMES)
            for symptome_item in symptomes_consultation:
                symptome = {
                    "id": symptome_item.id,
                    "libelle": symptome_item.libelle,
                    "description": symptome_item.description,
                    "created_at": symptome_item.created_at,
                    "updated_at": symptome_item.updated_at
                }
                data['symptomes'].append(symptome)

            maladies_consultation = self.foreign_elements(item.id, 'consultation_id',
                                                          self.CONSULTATION_MALADIES)
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
                data['maladies'].append(maladie)
            json_data['consultations'].append(data)

        return json_data



    def deserialize_output(self, output="FILE", path=base.OUTPUT_FILE):
        json_data = {
            "patients":[],
            "maladies": []
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
                praticien = self.get_element(consultation_item.praticien_id, self.PRATICIENS)
                consultations = {
                    "id": consultation_item.id,
                    "type": type.libelle if type != None else None,
                    "praticien": "{} {}".format(praticien.nom, praticien.prenom),
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

        for m_item in self.MALADIES:
            m = {
                "id": m_item.id,
                "libelle": m_item.libelle,
                "description": m_item.description,
                "symptomes":[],
                "created_at": m_item.created_at,
                "updated_at": m_item.updated_at
            }
            s_list = self.get_elements(m_item.symptomes, self.SYMPTOMES)
            for s_item in s_list:
                s = {
                    "id": s_item.id,
                    "libelle": s_item.libelle,
                    "description": s_item.description,
                    "created_at": s_item.created_at,
                    "updated_at": s_item.updated_at
                }
                m['symptomes'].append(s)

            json_data['maladies'].append(m)

        if output == "FILE":
            with open(path, 'w') as file:
                file.write(json.dumps(json_data, indent=4))
            return path
        elif output == "JSON":
            return json_data
