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

service = ServiceData.get_instance()#Charge les données du fichier db.json

def main():#La définition de la fonction est utile pour la récursivité

    #Menu principal
    affichage(["1- Maladie", "2- Consultation", "3- Charger un fichier csv", "4- Quitter le programme"])
    service.deserialize()
    #Saisie clavier
    principal = clavier([1, 2, 3, 4])

    if principal == 1:#Maladie
        # Menu maladie
        affichage(["1- Nouvelle maladie", "2- Maladies existantes"])
        # Saisie clavier
        maladie = clavier([1, 2])

        if maladie == 1:#Nouvelle maladie
            #Saisie nouvelle maladie
            saisie_maladie()

            #Relancement du programme
            main()
        else:#Maladies existantes
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

    elif principal == 2:#Consultation
        saisie_consultation()
        main()

    elif principal == 3:#Fichier CSV
        # Choix du fichier
        url = fichier()
        main()
    else:#Exit
        print("\nBye")


#Lancement du programme
main()