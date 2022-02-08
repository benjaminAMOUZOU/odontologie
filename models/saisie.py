"""Module Contenant les méthodes de saisie au clavier"""

__author__ = "Benjamin AMOUZOU"
__createAt__ = "07/02/2022"
__updateAt__ = "08/02/2022"

from maladie import Maladie
from symptome import Symptome
from data import MALADIES

#Fonction recupérant le choix d'un utilisateur en antier
def clavier(valeurs):
    operation = 0

    while True:
        operation = int(input("Quelle opération souhaitez-vous effectuer: "))
        if operation in valeurs:
            break

    return operation

#Fonction récupérant l'url sous forme de string
def fichier():
    url = input("Où se trouve le fichier (chemin absolu): ")
    return url

#Fonction pour la saisie en console d'une maladie
def saisieMaladie():
    while True:
        symptomes = []

        #Information de base d'une maladie
        libelle = input("\nQuel est le libellé de la maladie: ")
        description = input("\nVeuillez entrer une description pour maladie " + libelle + ": ")

        #Saisie des symptomes d'une maladie
        print("\nVeuillez renseigner les symptomes de la maladie " + libelle)
        while True:
            nbreSymptome = len(symptomes) + 1
            print("\nSymptome {}".format(nbreSymptome))

            lib = input("Libellé: ")
            des = input("Description: ")
            symptomes.append({"libelle": lib, "description": des})

            rep = input("\nAutre symptome(o/n): ")
            if rep == 'n':
                break

        #Renseignement des valeurs de la maladie
        id = 1
        if(len(MALADIES) > 0):
            id = len(MALADIES)
        maladie = Maladie(id, libelle, description)

        #Renseignement des symptomes de la maladie
        symp_id = 1
        for symp in symptomes:
            symptome = Symptome(symp_id, symp['libelle'], symp['description'])
            maladie.symptomes.append(symptome)
            symp_id += 1
        #Pas de saisie de traitement pour l'instant

        #Ajout de la maladie à la liste globale des maladies de l'application
        MALADIES.append(maladie)#Vérification de l'existence de la maladie prochainement

        print("\nLa maladie " + libelle + " a été ajoutée avec succès !")
        rep = input("\nAutre maladie(o/n): ")
        if rep == 'n':
            break