from untils.date import nowtostr
import json

class Personne:
    def __init__(self, id, nom, prenom, sexe, created_at=nowtostr(), updated_at=nowtostr()) -> None:
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe

        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return "{}".format(json.dumps(self.__dict__, indent=4))