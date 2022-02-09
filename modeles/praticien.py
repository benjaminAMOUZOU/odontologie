from modeles.personne import Personne
from untils.date import nowtostr
import json

class Praticien(Personne):
    def __init__(self, id, nom, prenom, sexe, email, password, created_at=nowtostr(), updated_at=nowtostr()) -> None:

        Personne.__init__(self, id, nom, prenom, sexe, created_at, updated_at)

        self.email = email
        self.password = password

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)

    def to_json(self):
        return json.dumps(self.__dict__, indent=4)
