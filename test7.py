M = [ [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0]]

def puissance4():
    while True:
        print(M[0][0],M[0][1],M[0][2],M[0][3],M[0][4]) 
        print(M[1][0],M[1][1],M[1][2],M[1][3],M[1][4]) 
        print(M[2][0],M[2][1],M[2][2],M[2][3],M[2][4]) 
        print(M[3][0],M[3][1],M[3][2],M[3][3],M[3][4]) 
        print(M[4][0],M[4][1],M[4][2],M[4][3],M[4][4]) 

        print("Joueur 1 : tapez la colonne où mettre votre jeton")
        choix=input()
        if choix == "1":
            if M[0][0] == (1,2):
                print("Colonnes déjà pleine")
            else:
                if M[1][0] == (1,2):
                    M[0][0] = 1
                else:
                    if M[2][0] == (1,2):
                        M[1][0] = 1
                    else:
                        if M[3][0] == (1,2):
                            M[2][0] = 1
                        else:
                            if M[4][0] == (1,2):
                                M[3][0] = 1
                            else:
                                M[4][0] = 1
                    
                

puissance4()