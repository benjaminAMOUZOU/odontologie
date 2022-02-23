from untils.date import nowtostr
import json


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

        self.symptomes = list()

    def set_simptomes(self, elements):
        self.symptomes = elements

    def foreign(self, consultation_id, maladie_id, traitement_id):
        self.consultation_id = consultation_id
        self.maladie_id = maladie_id
        self.traitement_id = traitement_id

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)

    def to_json(self):
        return json.dumps(self.__dict__, indent=4)
