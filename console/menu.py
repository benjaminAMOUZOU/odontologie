"""Module Contenant la fonction d'affichage des menus en console"""

__author__ = "Benjamin AMOUZOU"
__createAt__ = "07/02/2022"
__updateAt__ = "08/02/2022"

#Fonction affichant le menu en fonction des paramètres
def affichage(liste):
    for i in range(len(liste)):
        if i == 0:
            print("\n" + liste[i])#Affichage avec une ligne d'espace au début
        elif i == (len(liste) - 1):
            print(liste[i] + "\n")
        else:
            print(liste[i])#Affichage avec une ligne d'espace à la fin