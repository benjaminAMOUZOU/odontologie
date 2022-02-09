from structs.read import Serialize
from structs.service_data import ServiceData
from modeles import *

s = Serialize()
for item in s.get_praticiens():
    print(item)

for item in s.get_patients():
    print(item)

for item in s.get_maladies():
    print(item)

"""print(s.get_symptomes())
print(s.get_traitements())
print(s.get_consultations())
print(s.get_type_consultations())
print(s.get_consultation_maladie())"""

service = ServiceData.get_instance()
service.deserialize()
