from structs.service_data import ServiceData
from modeles import *

service = ServiceData.get_instance()

class ConsultationController:
    def __init__(self):
        pass

class MaladieController:
    def __init__(self, data):
        self.data = data

    def add_symptomes(self, element):
        pass

class SymptomeController:
    def __init__(self):
        pass