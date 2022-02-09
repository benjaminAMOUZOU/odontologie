from untils.date import nowtostr
import json

class TypeConsultation:
    def __init__(self, id, libelle, created_at=nowtostr(), updated_at=nowtostr()) -> None:
        self.id = id
        self.libelle = libelle

        self.created_at = created_at
        self.updated_at = updated_at

        self.consultations = list()

    def set_consultations(self, elements):
        self.consultations = elements

    def __str__(self):
        return "{}".format(json.dumps(self.__dict__, indent=4))