from date import nowtostr

class TypeConsultation:
    def __init__(self, id, libelle, created_at=nowtostr(), updated_at=nowtostr()) -> None:
        self.id = id
        self.libelle = libelle

        self.created_at = created_at
        self.updated_at = updated_at

        self.consultations = list()