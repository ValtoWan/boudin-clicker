Biblio = {}

def ajouterlivre():
    print("Saisissez le nom du livre :")
    nom=input()
    if nom in Biblio:
        print("Livre déjà dans notre base de données")
    else:
        print("Saisissez l'auteur :")
        auteur=input()
        Biblio[nom] = (auteur, "disponible")

def emprunter():
    print("Saisissez le nom du livre à emprunter :")
    nom=input()
    if nom in Biblio:
        if Biblio[nom][1] == "disponible":
            Biblio[nom] = "emprunté"
            print("Vous avec emprunter ",nom)
        else:
            print("Ce livre est déjà emprunté")

        
    else:
        print("Nous n'avons pas cet ouvrage")
       
def menu():
    while True:
        print("1 : Ajouter un livre")
        print("2 : Emprunter un livre")

        choix=input()
        if choix == "1":
            ajouterlivre()
        elif choix == "2":
            emprunter()

menu()