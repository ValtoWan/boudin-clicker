annuaire = {}

def ajouter():
    print("Entrer le nom :")
    nom=input()
    if nom in annuaire:
        print("Ce nom est déjà enregistré")
    else:
        print("Entrer le numero de téléphone :")
        numero=input()
        if numero.isdigit():
            annuaire[nom]=numero
            print("Contact ajouté !")
        else:
            print("numero invalide")

def rechercher():
    print("Entrer le nom")
    nom=input()
    if nom in annuaire:
        print(f"{nom}:{annuaire[nom]}")
    else:
        print("Contact introuvable")

def afficher():
    if annuaire:
        print("Contacts :")
        for nom, numero in annuaire.items():
            print(f"{nom} : {numero}")
    else:
        print("Aucun contact")

def modifier():
    if annuaire:
        print("Quel contact voulez-vous modifier ?")
        nom=input()
        if nom in annuaire:
            print("Nouveau numero :")
            nouveau=input()
            if nouveau.isdigit():
                print("Contact modifié !")
                annuaire[nom]=nouveau
            else:
                print("Numero invalide")
        else:
            print("Contact introuvable")

    else:
        print("Aucun contact")

def supprimer():
    if annuaire:
        print("Quel contact voulez-vous supprimer ?")
        nom=input()
        if nom in annuaire:
            print ("Contact supprimé")
            del annuaire[nom]
        else:
            print ("Contact introuvable")
    else:
        print("Aucun contact")


def menu():
    while True:
        print("1: Ajouter un contact")
        print("2: Rechercher un contact")
        print("3: Afficher tous les contacts")
        print("4: Modifier un contact")
        print("5: Supprimer un contact")
        print("6: Quitter")

        choix=input()

        if choix == "1":
            ajouter()
        elif choix == "2":
            rechercher()
        elif choix == "3":
            afficher()
        elif choix == "4":
            modifier()
        elif choix == "5":
            supprimer()
        elif choix == "6":
            print ("Merci, à bientôt !")
            break
        else:
            print("Mauvais saisie")

menu()

