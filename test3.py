list=[]

def statistique():
    while True:
        print("Entrez une note (négative pour terminer)")
        note=float(input())
        if note<0:
            break
        else:
            list.append(note)
            list.sort()
            print(list)

            nombre= len(list)
            print("Vous avez ", nombre, "notes dans votre liste")

            maximum=max(list)
            print("La note maximum est :", maximum)

            minimum=min(list)
            print("La note minimum est", minimum)

            somme=sum(list)
            moyenne=somme/nombre
            print("La moyenne des notes est", moyenne)


statistique()

    

