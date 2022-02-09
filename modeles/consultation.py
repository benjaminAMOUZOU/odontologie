from untils.date import nowtostr
import json

class Consultation:
    def __init__(self, id, observation, created_at=nowtostr(), updated_at=nowtostr()) -> None:
        self.id = id
        self.observation = observation

        self.type_id = 0
        self.patient_id = 0
        self.praticien_id = 0
        self.precedente_id = 0

        self.created_at = created_at
        self.updated_at = updated_at

        self.simptomes = list()

    def set_simptomes(self, elements):
        self.simptomes = elements

    def foreign(self, type_id, patient_id, praticien_id, precedente_id=None):
        self.type_id = type_id
        self.patient_id = patient_id
        self.praticien_id = praticien_id
        self.precedente_id = precedente_id

    def __str__(self):
        return "{}".format(json.dumps(self.__dict__, indent=4))

    """def __eq__(self, o: object) -> bool:
        return super().__eq__(o)"""

