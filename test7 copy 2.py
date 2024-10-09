M = [ [0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0] ]

def grid():
    for row in M:
        print(*row, sep="  ")

def jeton(colonne, joueur):
    for i in range(4, -1, -1):
        if M[i][colonne] == 0:
            M[i][colonne] = joueur
            return True
    return False

def jeu():
    joueur = 1
    while True:
        grid()

        print(f"Joueur {joueur} : choisissez la colonne (1-5)")
        try:
            colonne = int(input())-1
            if colonne < 0 or colonne > 4:
                print("Numéro colonne invalide.")
                continue
        except ValueError:
            print("Saisie invalide.")
            continue

        if jeton(colonne, joueur):
            joueur = 2 if joueur == 1 else 1
        else:
            print("Colonne déjà pleine.")

jeu()