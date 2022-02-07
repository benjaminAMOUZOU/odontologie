from untils.date import nowtostr

class Patient:
    def __init__(self, id, nom, prenom, sexe, date_naissance, groupSanguin, created_at=nowtostr(), updated_at=nowtostr()) -> None:
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe
        self.date_naissance = date_naissance
        self.groupSanguin = groupSanguin

        self.created_at = created_at
        self.updated_at = updated_at

        self.consultations: list()