M = [[0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0]]

def afficher_matrice():
    for ligne in M:
        print("   ".join(map(str, ligne)))

def puissance4():
    while True:
        afficher_matrice()

        print("Joueur 1 : tapez la colonne où mettre votre jeton :")
        choix = input()
        
        try:
            colonne = int(choix) - 1  
            if colonne < 0 or colonne > 4:
                print("Choix invalide, veuillez choisir entre 1 et 5.")
                continue

            for i in range(4, -1, -1):  
                if M[i][colonne] == 0:
                    M[i][colonne] = 1  
                    break
            else:
                print("Colonne déjà pleine.")
                continue
        
        except ValueError:
            print("Veuillez entrer un nombre valide.")
        
        afficher_matrice()
        
        print("Joueur 2 : tapez la colonne où mettre votre jeton :")
        choix = input()
        
        try:
            colonne = int(choix) - 1  
            if colonne < 0 or colonne > 4:
                print("Choix invalide, veuillez choisir entre 1 et 5.")
                continue

            for i in range(4, -1, -1):  
                if M[i][colonne] == (0):
                    M[i][colonne] = (2)  
                    break
            else:
                print("Colonne déjà pleine.")
                continue
        
        except ValueError:
            print("Veuillez entrer un nombre valide.")

puissance4()