from untils.date import nowtostr
import json

class Maladie:
    def __init__(self, id, libelle, description, created_at=nowtostr(), updated_at=nowtostr()) -> None:
        self.id = id
        self.libelle = libelle
        self.description = description

        self.created_at = created_at
        self.updated_at = updated_at

        self.symptomes = list()
        self.traitements = list()

    def set_simptomes(self, elements):
        self.symptomes = elements

    def set_traitements(self, elements):
        self.traitements = elements

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)

    def to_json(self):
        return json.dumps(self.__dict__, indent=4)