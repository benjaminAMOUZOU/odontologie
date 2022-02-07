from untils.date import nowtostr

class Maladie:
    def __init__(self, id, libelle, description, created_at=nowtostr(), updated_at=nowtostr()) -> None:
        self.id = id
        self.libelle = libelle
        self.description = description

        self.created_at = created_at
        self.updated_at = updated_at

        self.simptomes: list()
        self.traitements: list()