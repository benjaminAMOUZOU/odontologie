from models.date import nowtostr
from models.personne import Personne

class Patient(Personne):
    def __init__(self, id, nom, prenom, sexe, date_naissance, group_sanguin) -> None:

        Personne.__init__(self, id, nom, prenom, sexe)

        self.date_naissance = date_naissance
        self.group_sanguin = group_sanguin

        self.consultations = list()