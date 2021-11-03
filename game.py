print ("""Welkom in dit enge doolhof, maak je geen zorgen je komt heelhuids thuis.
""")

print ("""Gaat u links af of rechts af?
A. Links af
B. Rechts af""")
keuze = input(">>> ").lower()
if keuze == "a":
    print ("Onthoudt deze code. 5453")
    print ("Je komt een keypad tegen, voer een code in")
    keuze = input(">>> ").lower()
    if keuze == "5453":
        print ("Er gaat een deur open, ik denk dat de code goed is!")
        print ("""Gaat u links af of rechts af?
        A. Links af
        B. Rechts af""")
        keuze = input(">>> ").lower()
        if keuze == "a":
            print ("Je hebt de uitgang gevonden! Gelukkig!")
        elif keuze == "b":
            print ("Game-over | Begin opnieuw.")
    else:
        print ("Er gaat een valluik open!")
        print ("Game-over | Begin opnieuw.")
elif keuze == "b":
    print ("""Je ziet twee tools liggen, welke pak je?
    A. Zwaard
    B. Compas""")
    keuze = input(">>> ").lower()
    if keuze == "a":
        print ("""Je ziet een monster, ga je het gevecht aan of ga je vragen of je er langs mag.
        A. Gevecht
        B. Vragen of je er langs mag""")
        keuze = input(">>> ").lower()
        if keuze == "a":
            print ("Game-over | Begin opnieuw.")
        elif keuze == "b":
            print ("Hij laat je er langs!")
            print ("Je hebt de uitgang gevonden! Gelukkig!")
    elif keuze == "b":
        print ("""Gaat u links af of rechts af?
        A. Links af
        B. Rechts af""")
        keuze = input(">>> ").lower()
        if keuze == "a":
            print ("Game-over | Begin opnieuw.")
        elif keuze == "b":
            print ("Je hebt de uitgang gevonden! Gelukkig!")
else:
    print ("Game-over | Begin opnieuw.")