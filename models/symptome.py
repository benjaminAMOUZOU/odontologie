from date import nowtostr

class Symptome:
    def __init__(self, id, libelle, description, created_at=nowtostr(), updated_at=nowtostr()) -> None:
        self.id = id
        self.libelle = libelle
        self.description = description

        self.created_at = created_at
        self.updated_at = updated_at

        self.maladies = list()