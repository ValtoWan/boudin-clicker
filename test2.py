list = []
def courses():
    while True:
        print("Taper 1 pour ajouter un élément")
        print("Taper 2 pour retirer un élément")
        print("Taper 3 pour afficher la liste")
        print("Taper 4 pour quitter")
    


        choix=float(input())
        if choix==1:
            print("Que voulez-vous ajouter ?")
            element=(input())
            if element in list:                
                print(element, "est déja dans votre liste")
                
            else:
                list.append(element)
                print(element, "à été ajouté à votre liste")
                           
            
    
        elif choix==2:
            print("Que voulez-vous retirer ?")
            element=(input())
            if element in list:
                list.remove(element)
                print(element, "à été retiré de votre liste")
            else:
                print(element, "n'est pas dans votre liste")

    
        elif choix==3:
            print(list)

        elif choix==4:
            print("Merci, à bientôt !")
            break

        else:
            print("Choix invalide")




courses()