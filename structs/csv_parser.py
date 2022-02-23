from configs import base
from untils import file
from modeles.csv_base import CsvBase
from structs.service_data import ServiceData
from modeles import *
import csv

service = ServiceData.get_instance()

class CsvParser:
    def __init__(self, url):
        self.url = self.check_url(url)

        self.patient = None
        self.maladie = None
        self.symptomes = []
        self.consultation_maladie = None
        self.consultation = None

    def check_url(self, url):
        path = '{}/{}'.format(base.CSV_FILE_PATH, url)
        if not file.check_file_exit(path):
            if file.check_file_exit(url):
                return url
            else: return None
        else: return path

    def get_element(self, field, elements, value):
        for item in elements:
            if item.__dict__[field] == value:
                return item
        return None

    def get_elements(self, field, elements, value):
        items = []
        for item in elements:
            if item.__dict__[field] == value:
                items.append(item)
        return items

    def next_id(self, elementes):
        id = 1
        if (len(elementes) > 0):
            id = int(elementes[-1].id) + 1
        return id

    def init_value(self):
        self.patient = None
        self.maladie = None
        self.symptomes = []
        self.consultation_maladie = None
        self.consultation = None

    def runCsvBase(self, base : CsvBase):
        create_maladie = False

        self.patient = self.get_element("nom", service.PATIENTS, base.nom)
        if self.patient == None:
            self.patient = Patient(self.next_id(service.PATIENTS), base.nom, base.prenom, base.sexe, base.date_naissance, base.groupe_sanguin)
            service.PATIENTS.append(self.patient)

        if base.type_consulation.upper() == "NORMAL":
            self.maladie = self.get_element("libelle", service.MALADIES, base.maladie)
            if self.maladie == None:
                self.maladie = Maladie(self.next_id(service.MALADIES), base.maladie, "")
                create_maladie = True

            symptomes = base.symptomes.split('|')
            for symptome in symptomes:
                data = self.get_element("libelle", service.SYMPTOMES, symptome)
                if data == None:
                    data = Symptome(self.next_id(service.SYMPTOMES), symptome, "")
                    data.maladies.append(self.maladie.id)
                    self.maladie.symptomes.append(data.id)
                    service.SYMPTOMES.append(data)
                self.symptomes.append(data)

            if create_maladie: service.MALADIES.append(self.maladie)

            self.consultation = Consultation(self.next_id(service.CONSULTATIONS), "", created_at=base.date_consultation)
            self.consultation.symptomes = [item.id for item in self.symptomes]
            self.consultation.type_id = 1
            self.consultation.patient_id = self.patient.id

            self.consultation_maladie = ConsultationMaladie(self.next_id(service.CONSULTATION_MALADIES), base.date_premiere_consultation, '')
            self.consultation_maladie.consultation_id = self.consultation.id
            self.consultation_maladie.maladie_id = self.maladie.id
            self.consultation_maladie.symptomes = [item.id for item in self.symptomes]

            service.CONSULTATIONS.append(self.consultation)
            service.CONSULTATION_MALADIES.append(self.consultation_maladie)

        elif base.type_consulation.upper() == "REVISITE":

            self.consultation = Consultation(self.next_id(service.CONSULTATIONS), base.observation, created_at=base.date_consultation)
            self.consultation.type_id = 2

            tmp_consultation = self.get_elements("patient_id", service.CONSULTATIONS, self.patient.id)
            print(tmp_consultation)
            precedente = self.get_element("type_id", tmp_consultation, 1)
            print(precedente)
            self.consultation.precedente_id = precedente.id

            consultation_maladie = self.get_element('consultation_id', service.CONSULTATION_MALADIES, precedente.id)
            print(consultation_maladie)

            if consultation_maladie:
                consultation_maladie.fin_traitement = base.date_fin_traitement
                consultation_maladie.traitement_reussi = base.traite

            try:
                index = service.CONSULTATION_MALADIES.index(consultation_maladie)
                service.CONSULTATION_MALADIES[index] = consultation_maladie
            except:
                pass
            service.CONSULTATIONS.append(self.consultation)

    def run(self):
        fields = []
        rows = []
        if self.url:
            print("Log: {}".format(self.url))
            with open("{}".format(self.url), 'r') as file:
                csvreader = csv.reader(file)
                fields = next(csvreader)

                for row in csvreader:
                    csv_base = CsvBase(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13])
                    self.runCsvBase(csv_base)
                    self.init_value()
        else: print("\tFile Not Found")