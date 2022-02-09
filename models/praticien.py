from models.date import nowtostr
from models.personne import Personne

class Praticien(Personne):
    def __init__(self, id, nom, prenom, sexe, email, password) -> None:

        Personne.__init__(self, id, nom, prenom, sexe)

        self.email = email
        self.password = password
