from sturct.read import Serialize

s = Serialize()

print(s.get_praticiens())
print(s.get_patients())
print(s.get_maladies())
print(s.get_symptomes())
print(s.get_traitements())
print(s.get_consultations())
print(s.get_consultations_type())
print(s.get_consultation_maladie())