"""Module Contenant les méthodes de saisie au clavier"""

__author__ = "Benjamin AMOUZOU"
__createAt__ = "07/02/2022"
__updateAt__ = "09/02/2022"

from modeles.maladie import Maladie
from modeles.symptome import Symptome
from modeles.traitement import Traitement
from console.data import MALADIES
from console.data import SYMPTOMES
from console.data import TRAITEMENTS

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
def saisie_maladie():
    while True:
        libelle = ""
        description = ""
        symptomes = []
        traitements = []

        #Saisie des informations atomiques d'une maladie
        while True:
            libelle = input("\nQuel est le libellé de la maladie: ")
            if len(libelle) > 0:
                break
        description = input("\nVeuillez entrer une description pour maladie " + libelle + ": ")
        #Fin saisie des informations atomiques d'une maladie

        #Saisie des symptomes d'une maladie
        print("\nVeuillez renseigner les symptomes de la maladie " + libelle)
        while True:
            print("\nSymptome {}".format(len(symptomes) + 1))

            while True:#Libellé non null, description oui
                lib = input("Libellé: ")
                if len(lib) > 0:
                    break
            des = input("Description: ")
            symptomes.append({"libelle": lib, "description": des})

            rep = input("\nAutre symptome(o/n): ")
            if rep == 'n':
                break
        #Fin saisie des symptomes d'une maladie

        #Saisie des traitements d'une maladie(Facultatif)
        rep = input("\nVoulez-vous renseigner les traitements possibles pour la maladie " + libelle + " (o/n): ")
        if rep == 'o':
            while True:
                print("\nTraitement {}".format(len(traitements) + 1))

                while True:  #Libellé non null, description oui
                    lib = input("Libellé: ")
                    if len(lib) > 0:
                        break
                des = input("Description: ")
                traitements.append({"libelle": lib, "description": des})

                rep = input("\nAutre traitement(o/n): ")
                if rep == 'n':
                    break
        #Fin saisie des traitements d'une maladie

        #Initialisation des valeurs atomiques de l'objet maladie
        id = 1
        if(len(MALADIES) > 0):
            id = len(MALADIES) + 1
        maladie = Maladie(id, libelle, description)

        #Initialisation des symptomes de l'objet maladie
        symp_id = 1
        if(len(SYMPTOMES) > 0):
            symp_id = len(SYMPTOMES) + 1

        for symp in symptomes:
            symptome = Symptome(symp_id, symp['libelle'], symp['description'])
            maladie.symptomes.append(symptome.id)
            symp_id += 1

            SYMPTOMES.append(symptome)
        #Fin Initialisation des symptomes de l'objet maladie

        #Initialisation des traitements de la maladie
        trait_id = 1
        if (len(TRAITEMENTS) > 0):
            trait_id = len(TRAITEMENTS) + 1

        for trait in traitements:
            traitement = Traitement(trait_id, trait['libelle'], trait['description'])
            maladie.traitements.append(traitement.id)
            trait_id += 1

            TRAITEMENTS.append(traitement)
        #Fin initialisation des traitemens de la maladie

        #Ajout de la maladie à la liste globale des maladies de l'application
        MALADIES.append(maladie)#Vérification de l'existence de la maladie prochainement
        print(maladie)#A supprimer

        print("\nLa maladie " + libelle + " a été ajoutée avec succès !")
        rep = input("\nAutre maladie(o/n): ")
        if rep == 'n':
            break
#Fin fonction pour la saisie en console d'une maladie

#Fonction pour la saisie en console d'une consultation
def saisie_consultation():
    #
    print("")