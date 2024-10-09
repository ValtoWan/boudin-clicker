prixaukilo=12.5

def discussion():
    print ("Bonjour  Madame, combien de kilos de boudin aujourd'hui ?")
    Quantitédeboudin = float(input())
    print ("Le prix au kilo est de ", prixaukilo, " euros")
    prixduboudin=prixaukilo*Quantitédeboudin
    print ("Le prix total est de ", prixduboudin, " euros ")
    Pourboire = float(input("Voulez-vous donner un pourboire ?"))
    total = prixduboudin + Pourboire
    print ("Cela fera donc", total, "euros")
discussion()