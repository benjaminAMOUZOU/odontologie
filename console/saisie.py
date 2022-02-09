"""Module Contenant les méthodes de saisie au clavier"""

__author__ = "Benjamin AMOUZOU"
__createAt__ = "07/02/2022"
__updateAt__ = "09/02/2022"

from modeles.maladie import Maladie
from modeles.symptome import Symptome
from modeles.traitement import Traitement
from modeles.patient import Patient
from structs.service_data import ServiceData

service = ServiceData.get_instance()

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
        if(len(service.MALADIES) > 0):
            id = int(service.MALADIES[-1].id) + 1
        maladie = Maladie(id, libelle, description)

        #Initialisation des symptomes de l'objet maladie
        symp_id = 1
        if(len(service.SYMPTOMES) > 0):
            symp_id = int(service.SYMPTOMES[-1].id) + 1

        for symp in symptomes:
            symptome = Symptome(symp_id, symp['libelle'], symp['description'])
            maladie.symptomes.append(symptome.id)
            symp_id += 1

            service.SYMPTOMES.append(symptome)
        #Fin Initialisation des symptomes de l'objet maladie

        #Initialisation des traitements de la maladie
        trait_id = 1
        if (len(service.TRAITEMENTS) > 0):
            trait_id = service.TRAITEMENTS[-1].id + 1

        for trait in traitements:
            traitement = Traitement(trait_id, trait['libelle'], trait['description'])
            maladie.traitements.append(traitement.id)
            trait_id += 1

            service.TRAITEMENTS.append(traitement)
        #Fin initialisation des traitemens de la maladie

        #Ajout de la maladie à la liste globale des maladies de l'application
        service.MALADIES.append(maladie)#Vérification de l'existence de la maladie prochainement
        print(maladie)#A supprimer

        print("\nLa maladie " + libelle + " a été ajoutée avec succès !")
        rep = input("\nAutre maladie(o/n): ")
        if rep == 'n':
            break
#Fin fonction pour la saisie en console d'une maladie

#Fonction pour la saisie en console d'une consultation
def saisie_consultation():
    affichage(["1- Nouveau patient", "2- Ancien patient"])
    print("")
#Fin fonction pour la saisie en console d'une consultation

#Fonction pour la saisie d'un patient
def saisie_patient():#Un seul patient à la fois
    nom = input("Nom du patient: ")
    prenom = input("Prénom du patient: ")
    date_naissance = input("Date de naissance du patient(dd-mm-yyyy): ")
    sexe = input("Sexe du patient: ")
    group_sanguin = input("Groupe sanguin du patient: ")

    id = 1
    if len(PATIENTS) > 0:
        id = int(PATIENTS[-1].id) + 1

    return Patient(id, nom, prenom, sexe, date_naissance, group_sanguin)
#Fin fonction pour la saisie d'un patient