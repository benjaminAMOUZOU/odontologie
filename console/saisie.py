"""Module Contenant les méthodes de saisie au clavier"""

__author__ = "Benjamin AMOUZOU"
__createAt__ = "07/02/2022"
__updateAt__ = "15/02/2022"

from modeles.maladie import Maladie
from modeles.symptome import Symptome
from modeles.traitement import Traitement
from modeles.patient import Patient
from modeles.consultation import Consultation
from structs.service_data import ServiceData
from console.menu import affichage

service = ServiceData.get_instance()

#Fonction recupérant le choix d'un utilisateur en antier
def clavier(valeurs):
    operation = 0

    while True:
        operation = int(input("Quel est votre choix: "))
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
        description = input("\nVeuillez entrer une description pour la maladie " + libelle + "(Facultatif): ")
        #Fin saisie des informations atomiques d'une maladie

        #Saisie des symptomes d'une maladie
        print("\nVeuillez renseigner les symptomes de la maladie " + libelle)
        while True:
            print("\nSymptome {}".format(len(symptomes) + 1))

            while True:#Libellé non null, description oui
                lib = input("Libellé: ")
                if len(lib) > 0:
                    break
            des = input("Description(Facultatif): ")
            symptomes.append({"libelle": lib, "description": des})

            rep = input("\nAutre symptome ? [o/n]: ")
            if rep == 'n':
                break
        #Fin saisie des symptomes d'une maladie

        """#Saisie des traitements d'une maladie(Facultatif)
        rep = input("\nVoulez-vous renseigner les traitements possibles pour la maladie " + libelle + " ? [o/n]: ")
        if rep == 'o':
            while True:
                print("\nTraitement {}".format(len(traitements) + 1))

                while True:  #Libellé non null, description oui
                    lib = input("Libellé: ")
                    if len(lib) > 0:
                        break
                des = input("Description: ")
                traitements.append({"libelle": lib, "description": des})

                rep = input("\nAutre traitement? [o/n]: ")
                if rep == 'n':
                    break
        #Fin saisie des traitements d'une maladie"""

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

        """"#Initialisation des traitements de la maladie
        trait_id = 1
        if (len(service.TRAITEMENTS) > 0):
            trait_id = service.TRAITEMENTS[-1].id + 1

        for trait in traitements:
            traitement = Traitement(trait_id, trait['libelle'], trait['description'])
            maladie.traitements.append(traitement.id)
            trait_id += 1

            service.TRAITEMENTS.append(traitement)
        #Fin initialisation des traitemens de la maladie"""

        #Ajout de la maladie à la liste globale des maladies de l'application
        service.MALADIES.append(maladie)#Vérification de l'existence de la maladie prochainement
        print(maladie)#A supprimer

        print("\nLa maladie " + libelle + " a été ajoutée avec succès !")
        rep = input("\nAutre maladie ? [o/n]: ")
        if rep == 'n':
            break
#Fin fonction pour la saisie en console d'une maladie

#Fonction pour la saisie en console d'une consultation
def saisie_consultation(praticien_courant):
    affichage(["1- Nouveau patient", "2- Ancien patient"])
    rep = clavier([1, 2])

    #Création de la consultation
    id = 1
    if len(service.CONSULTATIONS) > 0:
        id = int(service.CONSULTATIONS[-1].id) + 1
    consultation = Consultation(id, "")
    consultation.praticien_id = praticien_courant.id

    if rep == 1:#Nouveau patient
        #Saisie des informations du nouveau patient
        patient = saisie_patient()

        #Affectation des valeurs à la consultation
        consultation.patient_id = patient.id
        consultation.type_id = 1
        consultation.symptomes = saisie_symptome_patient(patient)

        #Et de la consultation au patient
        patient.consultations.append(consultation.id)

        #Maladie et MaladieTraitement                                                               =>=>=>=>=>=>=>=>=>=>
        # Affectation à la liste des consultations
        service.CONSULTATIONS.append(consultation)

    else:#Ancien patient

        if len(service.PATIENTS) == 0:#Aucun patient
            print("\nAucun patient précédement enrégister !")
        else:
            #Liste des patients
            liste_patients = []
            liste_choix = []
            for patient in service.PATIENTS:
                liste_patients.append("{}- {} {}".format(patient.id, patient.nom, patient.prenom))
                liste_choix.append(patient.id)

            #Choix du patient déjà enrégistrer
            affichage(liste_patients)
            patient_id = clavier(liste_choix)
            consultation.patient_id = patient_id

            #Normal ou Revisite ?
            affichage(["1- Nouvelle consultation ?", "2- Revisite ?"])
            type_consultation = clavier([1, 2])

            if type_consultation == 2:#Revisite
                consultation.type_id = 2

                while True:
                    date_consultation = input("\nQuelle était la date de la toute première consultation (dd-mm-aaaa) : ")

                    #recherche de l'identifiant de la première consultation puis affectation
                    consultation_precedente_trouve = False
                    for cons in service.CONSULTATIONS:
                        if cons.patient_id == consultation.patient_id and consultation.created_at.split(" ")[0] == date_consultation:
                            consultation_precedente_trouve = True
                            consultation.precedente_id = cons.id
                            #Saisie de l'observation pour la revisite
                            consultation.observation = input("\nUne observation pour cette revisite : ")

                            #Affectation de la consultation à la liste des consultations du patient
                            for index, patient in enumerate(service.PATIENTS):
                                if patient.id == consultation.patient_id:
                                    service.PATIENTS[index].consultations.append(consultation.id)
                            #Maladie, ConsultationMaladie, Praticien                                =>=>=>=>=>=>=>=>=>=>
                            service.CONSULTATIONS.append(consultation)
                            break

                    #Message d'erreur
                    if not consultation_precedente_trouve:
                        print("\nAucune correpondance pour la date {} !".format(date_consultation))

                        # Reprise
                        rep = input("\nSaisir à nouveau la date de la première consultation ? [o/n]: ")
                        if rep == 'n':
                            break
                    else:
                        break

            else:#Consultation normale
                consultation.type_id = 1
                #Affectation de la nouvelle consultation à l'ancien patient
                pat = {}
                for index, patient in enumerate(service.PATIENTS):
                    if patient.id == consultation.patient_id:
                        pat = patient;
                        service.PATIENTS[index].consultations.append(consultation.id)
                #Saisie des nouveaux symptomes de  l'ancien patient
                consultation.symptomes = saisie_symptome_patient(pat)
                #Maladie, ConsultationMaladie, Praticien                                            =>=>=>=>=>=>=>=>=>=>
                service.CONSULTATIONS.append(consultation)
#Fin fonction pour la saisie en console d'une consultation

#Fonction pour la saisie d'un patient
def saisie_patient():#Un seul patient à la fois
    nom = input("\nNom du patient: ")
    prenom = input("Prénom du patient: ")
    date_naissance = input("Date de naissance du patient (dd-mm-yyyy): ")
    sexe = input("Sexe du patient (M/F): ")
    group_sanguin = input("Groupe sanguin du patient: ")

    id = 1
    if len(service.PATIENTS) > 0:
        id = int(service.PATIENTS[-1].id) + 1

    patient = Patient(id, nom, prenom, sexe, date_naissance, group_sanguin);

    #Vérification de la non existence du patient
    for pat in service.PATIENTS:
        if pat.nom == patient.nom and pat.prenom == patient.prenom and pat.nom == patient.date_naissance:
            patient = pat
    service.PATIENTS.append(patient)

    return patient
#Fin fonction pour la saisie d'un patient

#Fonction pour la saisie des symtomes du patient
def saisie_symptome_patient(patient):
    symptomes = []#ids des symptomes du patient utile pour l'association à la consultation

    print('\nQuels sont les symptomes du patient ' + patient.nom + ' ?')
    while True:
        exist = False
        symptome_libelle = input('\nSymptome {} : '.format(len(symptomes) + 1))

        #Vérification de l'existence du symptome dans la liste
        for symp in service.SYMPTOMES:
            if symp.libelle == symptome_libelle:#Le symptome exist déjà
                symptomes.append(symp.id)#Affectation de l'id à symptomes qui est retourné à la fin de la fonction
                exist = True
                break

        #Création de l'objet symptome
        if exist == False:
            #Déclaration
            symptome_id = 1
            symptome = {}

            if len(service.SYMPTOMES) > 0:
                symptome_id = int(service.SYMPTOMES[-1].id) + 1

            symptome = Symptome(symptome_id, symptome_libelle, "")
            print("\nLe symptome n'existe pas encore dans le système ! A quelle maladie ce symptome est-il lié ? :")

            if len(service.MALADIES) > 0:
                affichage(["1- Maladies existantes", "2- Nouvelle maladie"])
                saisie = clavier([1, 2])

                if saisie == 1:#Maladies existantes pour ce symptome
                    list_maladies = []#Juste pour appeler affichage() et clavier()
                    id_maladies = []

                    #Affichage des maladies, choix de la maladie et association du symtome à cette maladie
                    for maladie in service.MALADIES:
                        list_maladies.append("{} - {}".format(maladie.id, maladie.libelle))
                        id_maladies.append(maladie.id)

                    affichage(list_maladies)
                    maladie_id = clavier(id_maladies)

                    #Association de la maladie au symptome
                    symptome.maladies.append(maladie_id)

                    #Et du symptome à la maladie
                    for index, maladie in enumerate(service.MALADIES):
                        if maladie.id == maladie_id:
                            service.MALADIES[index].symptomes.append(symptome.id)

                    # Ajout du symptome à la liste globale des symptomes
                    service.SYMPTOMES.append(symptome)
                    symptomes.append(symptome.id)

                else:#Nouvelle maladie pour ce symptome
                    maladie_libelle = input("\nQuelle est le libellé d'une maladie associée à ce symptome : ")
                    maladie_description = input("\nQuelle est la description de la maladie {} associée à ce symptome(facultatif) : ".format(maladie_libelle))
                    maladie_id = int(service.MALADIES[-1].id) + 1

                    #Création de la nouvelle maladie
                    maladie = Maladie(maladie_id, maladie_libelle, maladie_description)
                    maladie.symptomes.append(symptome.id)
                    service.MALADIES.append(maladie)#Ajout de la maladie à la liste globale service.MALADIES.

                    # Association de la maladie au symptome
                    symptome.maladies.append(maladie.id)
                    service.SYMPTOMES.append(symptome)  # Ajout du symptome à la liste globale des symptomes
                    symptomes.append(symptome.id)
                # Fin saisie == 1

            else:#Il n'y a encore aucune maladie dans le fichier json
                maladie_libelle = input("\nQuelle est le libellé d'une maladie associée à ce symptome : ")
                maladie_description = input("\nQuelle est la description de la maladie {} associée à ce symptome[facultatif] : ".format(maladie_libelle))

                #Création de la nouvelle maladie
                maladie = Maladie(1, maladie_libelle, maladie_description)
                maladie.symptomes.append(symptome.id)
                service.MALADIES.append(maladie) #Ajout du symptome à la liste globale des maladies
                symptome.maladies.append(1)
                service.SYMPTOMES.append(symptome) #Ajout du symptome à la liste globale des symptomes
                symptomes.append(symptome.id)#A retourner
            #Fin if len(service.MALADIES > 0):
        #Fin if exist == False:

        rep = input("\nAutre symptome ? [o/n]: ")
        if rep == 'n':
            break

    return symptomes
#Fin fonction pour la saisie des symtomes du patient