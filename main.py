# -*- coding: utf-8 -*-
"""Point d'entrée du programme"""

__author__ = "Benjamin AMOUZOU"
__createAt__ = "07/02/2022"
__updateAt__ = "09/02/2022"

from console.saisie import clavier
from console.saisie import fichier
from console.saisie import saisie_maladie
from console.saisie import saisie_consultation
from console.menu import affichage
from structs.service_data import ServiceData
from modeles import *

print("\n***********************************************")
print("Structuration des données: Cas de l'odontologie")
print("***********************************************")

service = ServiceData.get_instance()

def main():#La définition de la fonction est utile pour la récursivité
    """Avant de proposer le menu charger les donnees du fichier
    json dans les variables globales du module data"""

    #Menu principal
    affichage(["1- Maladie", "2- Consultation", "3- Charger un fichier xlsx", "4- Quitter le programme"])

    service.deserialize() # Ecriure du fichier a chaque fois qu'on reviens au menu
    service.deserialize_output()

    #Saisie clavier
    principal = clavier([1, 2, 3, 4])

    if principal == 1:
        # Menu maladie
        affichage(["1- Nouvelle maladie", "2- Maladies existantes"])
        # Saisie clavier
        maladie = clavier([1, 2])

        if maladie == 1:
            #Saisie nouvelle maladie
            saisie_maladie()

            #Relancement du programme
            main()
        else:
            #Liste des maladies existantes
            print("\nListe des maladies existantes")
            print("-----------------------------\n")
            if len(service.MALADIES) > 0:
                for maladie in service.MALADIES:
                    print(maladie)#Rédéfinir la méthode correspondante dans la classe Maladie
            else:
                print("Aucune maladie enrégistrée !\n")

            #Relancement du programme
            main()

    elif principal == 2:
        # Menu consultation
        affichage(["1- Nouvelle consultation", "2- Consultations existantes"])
        # Saisie clavier
        consultation = clavier([1, 2])

        if(consultation == 1):
            saisie_consultation()
            main()
        else:
            pass
    elif principal == 3:
        # Choix du fichier
        url = fichier()
        main()
    else:
        print("\nBye")


#Lancement du programme
main()