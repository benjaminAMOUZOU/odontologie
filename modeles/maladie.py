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

    def __str__(self):
        return "{}".format(json.dumps(self.__dict__, indent=4))