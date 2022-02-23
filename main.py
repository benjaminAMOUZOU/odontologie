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
import getpass

print("\n***********************************************")
print("Structuration des données: Cas de l'odontologie")
print("***********************************************")

service = ServiceData.get_instance()#Charge les données du fichier db.json
praticien_courant = {}#Praticien courant
first_execution = True;#Première exécution du main
connecte = False;#Pour vérifier si le praticien est connecté

def main(connecte,first_execution, praticien_courant):#La définition de la fonction est utile pour la récursivité

    if(first_execution):
        first_execution = False
        email = input("\nEmail: ")
        if(len(service.PRATICIENS) == 0):
            #Création et affectation du praticien à praticien_courant
            praticien_courant = saisie_info_praticien(email)#Chiffrer le mot de passe plus tard
            service.PRATICIENS.append(praticien_courant)
            print("\nConnecté en tant que {} {} \n".format(praticien_courant.nom, praticien_courantprenom))
            connecte = True
        else:
            trouve = False
            #Récupération des informations de connexion du praticien
            for praticien in service.PRATICIENS:
                if email == praticien.email:
                    while True:
                        password = getpass.getpass("\nMot de passe: ")
                        if(password == praticien.password):
                            praticien_courant = praticien
                            print("\nConnecté en tant que {} {} \n".format(praticien_courant.nom, praticien_courant.prenom))
                            trouve = True
                            connecte = True
                            break
                        else:
                            print("\nMot de passe incorrect !")
                    break

            if(not trouve):#Adresse mail pas dans la liste
                print("\nAdresse email n'ont présente dans le système !")
                praticien_courant = saisie_info_praticien(email)  # Chiffrer le mot de passe plus tard
                service.PRATICIENS.append(praticien_courant)
                print("\nConnecté en tant que {} {} \n".format(praticien_courant.nom, praticien_courant.prenom))
                connecte = True

    if(connecte):
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
                main(connecte,first_execution, praticien_courant)
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
                main(connecte,first_execution, praticien_courant)

        elif principal == 2:#Consultation
            saisie_consultation(praticien_courant)
            main(connecte,first_execution, praticien_courant)

        elif principal == 3:#Fichier CSV
            # Choix du fichier
            url = fichier()
            main(connecte,first_execution, praticien_courant)
        else:#Exit
            print("\nBye")

#Fonction de saisie des informations du praticien
def saisie_info_praticien(email):
    id = 1
    if len(service.PATIENTS) > 0:
        id = int(service.PATIENTS[-1].id) + 1
    # Création du nouveau praticien
    print("\n***Saisie des informations du nouveau praticien***")
    nom = input("Nom: ")
    prenom = input("Prénom: ")
    sexe = input("Sexe (M/F): ")
    password = getpass.getpass("Mot de passe: ")

    return Praticien(id, nom, prenom, sexe, email, password)
#Fin Fonction de saisie des informations du praticien

#Lancement du programme
main(connecte,first_execution,praticien_courant)