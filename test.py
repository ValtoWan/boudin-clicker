def calcul():
    print("Entrez le premier nombre :")
    premiernombre = float(input())

    

    print("quel opération voulez-vous faire ?")
    opération = (input())
    

    print("Entrez le deuxième nombre :")
    deuxiemenombre = float(input())

    if opération == "*":
        Résultat = premiernombre*deuxiemenombre
    elif opération == "-":
        Résultat = premiernombre-deuxiemenombre
    elif opération == "+":
        Résultat = premiernombre+deuxiemenombre
    elif opération == "/":
        if deuxiemenombre != 0:
            Résultat = premiernombre+deuxiemenombre
        else:
            print("erreur")

    print("Le résultat est :",Résultat)
calcul()
