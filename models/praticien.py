from date import nowtostr

class Praticien:
    def __init__(self, id, nom, prenom, sexe, email, password, created_at=nowtostr(), updated_at=nowtostr()) -> None:
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe
        self.email = email
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at
