from date import nowtostr

class ConsultationMaladie:
    def __init__(self, id, debut_traitement, fin_traitement, traitement_reussi=False, created_at=nowtostr(), updated_at=nowtostr()) -> None:
        self.id = id
        self.debut_traitement = debut_traitement
        self.fin_traitement = fin_traitement
        self.traitement_reussi = traitement_reussi

        self.consultation_id = 0
        self.maladie_id = 0
        self.traitement_id = 0

        self.created_at = created_at
        self.updated_at = updated_at

        self.simptomes: list()

    def foreign(self, consultation_id, maladie_id, traitement_id):
        self.consultation_id = consultation_id
        self.maladie_id = maladie_id
        self.traitement_id = traitement_id
