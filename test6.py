def analyse():
    print("Saisissez votre texte :")
    textbrut=input()
    text=textbrut.lower()
    nombredelettres=sum(1 for char in text if char.isalpha())

    
    
    mots = [mot.strip(",.!?") for mot in text.split() if mot.strip(",.!?")]
    nombredemots=len(mots)


    nombre1=text.count(".")
    nombre2=text.count("?")
    nombre3=text.count("!")
    nombredephrases=nombre1+nombre2+nombre3

    print("Nombre de lettres : ",nombredelettres)
    print("Nombres de mots : ",nombredemots)
    print("Nombres de phrases : ",nombredephrases)


analyse()