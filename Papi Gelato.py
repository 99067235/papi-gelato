# Jurrian Schouten
# 99067235

import time
import webbrowser

e = 0
i = 0

prijsBolletjes = 0.95
prijsHorrentjes = 1.25
prijsBakje = 0.75
hoorntje = 0
bakje = 0
totaalBolletjes = 0
toppingKosten = 0.00
aantalToppings = 0
lijstMetToppings = ["sr", "slagroom", "sp", "sprinkels", "cs", "caramelsaus"]
kostenBakje = 0
kostenHoorntje = 0
kostenToppings = 0
kostenBolletjes = 0
HoeveelLiter = 0
smaak = ""
antwoord3 = ""
Btw = 6
btwprijs = 0


def sorry():
    print("Sorry, zulke grote bakken hebben we niet")
    

def snapNiet():
    print("Sorry, dat is geen optie die we aanbieden...")



def topping(bolletjes):
    global aantalToppings
    global toppingKosten
    global antwoord3
    toppingKeuze = input("Wat voor topping wilt u: G) Geen, SR) Slagroom, SP) Sprinkels of CS) Caramel Saus? ").lower()
    if toppingKeuze == "g":
        print("")
        
    elif toppingKeuze in lijstMetToppings:
        aantalToppings += 1

        if toppingKeuze == "sr" or toppingKeuze == "slagroom":
            toppingKosten += 0.50

        elif toppingKeuze == "sp" or toppingKeuze == "sprinkels":
            toppingKosten += (0.30 * bolletjes)

        elif toppingKeuze == "cs" or toppingKeuze == "caramelsaus":
            if antwoord3 == "B":
                toppingKosten += 0.90

            elif antwoord3 == "A":
                toppingKosten += 0.60
            
            else:
                print("foutje")

        else:
            snapNiet()
    else:
        snapNiet()
        topping(bolletjes)

def bonParticulier():
    global kostenBakje
    global kostenToppings
    global kostenHoorntje
    global kostenBolletjes
    global i
    global e
    print("Bedankt en tot ziens!")
    print("---------[Papi Gelato]---------")
    kostenBolletjes = float(totaalBolletjes * prijsBolletjes)
    print("Bolletjes:   "  ,  totaalBolletjes, "X",  prijsBolletjes,  "= €",   float(totaalBolletjes) * prijsBolletjes)
    if hoorntje >= 1:
        kostenHoorntje = hoorntje * prijsHorrentjes
        print("Horrentjes:  ",  hoorntje, "X",  prijsHorrentjes, "= €",   kostenHoorntje)
    if bakje >= 1:
        kostenBakje = bakje * prijsBakje
        print("Bakje:       "     ,  bakje, "X",  prijsBakje,      "= €",   kostenBakje)
    if aantalToppings >= 1:
        kostenToppings = float(aantalToppings) * toppingKosten
        print("Topping:     "   ,  aantalToppings, "X", toppingKosten, "= €", kostenToppings)
    print("             --------------------- +")
    print("Totaal       = €",kostenBolletjes + kostenHoorntje + kostenBakje + kostenToppings)
    i = 1
    e = 1

def bonZakelijk():
    global HoeveelLiter
    global i
    prijs = HoeveelLiter * 9.80
    btw = prijs / 100 * 6
    print("Bedankt en tot ziens!")
    print("---------[Papi Gelato]---------")
    print("Liter:  ", HoeveelLiter, "X €","9,80", " = €", prijs)
    print("             -------------- +")
    print("Totaal               = €", prijs)
    btwprijs = round(float(prijs/100 * Btw),2)
    print("BTW (6%)             = €", btwprijs)
    exit()

def bakjeGekozen(bolletjes):
    global bakje
    bakje += 1
    topping(bolletjes)
    antwoord4 = input("Hier is uw bakje met "+ str(bolletjes) +" bolletje(s). Wilt u nog meer bestellen? (Y/N)").upper()
    if antwoord4 == "Y":
        print("")
    elif antwoord4 == "N":
        bonParticulier()
        exit()
    else:
        sorry()
        bakjeGekozen(bolletjes)

def hoorntjeMeerbestellen(bolletjes):
    antwoord4 = input("Hier is uw hoorntje met "+ str(bolletjes) +" bolletje(s). Wilt u nog meer bestellen? (Y/N)").upper()
    if antwoord4 == "Y":
        print("")
    elif antwoord4 == "N":
        bonParticulier()
        exit()
    else:
        snapNiet()
        hoorntjeMeerbestellen()

def keuzeVerpakking(bolletjes):
    global hoorntje
    global antwoord3
    antwoord3 = input("Wilt u deze "+ str(bolletjes) +" bolletje(s) in A) een hoorntje of B) een bakje? ").upper()
    if antwoord3 == "A":
        hoorntje += 1
        topping(bolletjes)
        hoorntjeMeerbestellen(bolletjes)
    elif antwoord3 == "B":
        bakjeGekozen(bolletjes)
    else:
        snapNiet()
        keuzeVerpakking(bolletjes)

def welkeSmaak(bolletjes):
    try:
        for i in range(1,bolletjes + 1):
            print("Welke smaak wilt u voor bolletje nummer", str(i), "A) Aardbei, C) Chocolade, of V) Vanille?")
            smaak = input("Vul hier uw antwoord in: " ).upper()
            if smaak != "A" and smaak != "C" and smaak != "M" and smaak != "V":
                snapNiet()
                welkeSmaak(bolletjes)
        keuzeVerpakking(bolletjes)
    except ValueError:
        snapNiet()
        welkeSmaak(bolletjes)

def bakjeMeerBestellen(bolletjes):
    global antwoord3
    topping(bolletjes)
    antwoord4 = input("Hier is uw bakje met "+ str(bolletjes) +" bolletje(s). Wilt u nog meer bestellen? (Y/N)").upper()
    if antwoord4 == "Y":
        print("")
    elif antwoord4 == "N":
        bonParticulier()
        exit()
    else:
        snapNiet()
        bakjeMeerBestellen(bolletjes)

def welkeSmaakGroot(bolletjes):
    global bakje
    global smaak
    global antwoord3
    try:
        for i in range(1,bolletjes + 1):
            print("Welke smaak wilt u voor bolletje nummer", str(i), "A) Aardbei, C) Chocolade, of V) Vanille?")
            smaak = input("Vul hier uw antwoord in: " ).upper()
            if smaak != "A" and smaak != "C" and smaak != "M" and smaak != "V":
                bakje = 1
                snapNiet()
                welkeSmaakGroot(bolletjes)
        bakjeMeerBestellen(bolletjes)
    except ValueError:
        snapNiet()
        welkeSmaakGroot()


def aantalbolletjes():
    global totaalBolletjes
    global antwoord3
    try:
        bolletjes = int(input("Hoeveel bolletjes wilt u? "))
        if bolletjes <= 3 and bolletjes >= 0:
            totaalBolletjes += bolletjes
            welkeSmaak(bolletjes)
        elif bolletjes > 3 and bolletjes <= 8:
            totaalBolletjes += bolletjes
            print("Dan krijgt u van mij een bakje met", bolletjes, "bolletjes")
            welkeSmaakGroot(bolletjes)
        elif bolletjes <= 0:
            print("Helaas verkopen wij geen hoorntjes of bakjes met minder dan 1 bolletje.")
            bolletjes = 0
        elif bolletjes > 8:
            sorry()
            aantalbolletjes()
            bolletjes = 0
        else:
            snapNiet()
            bolletjes = 0
    except ValueError:
        snapNiet()
        aantalbolletjes()

def hoeveelLiter():
    global HoeveelLiter
    try:
        HoeveelLiter = int(input("Hoeveel liter ijs wilt u bestellen? "))
        if HoeveelLiter >= 1:
            for f in range(1, HoeveelLiter + 1):
                print("Welke smaak wilt u voor liter", (f), "A) Aardbei, C) Chocolade, of V) Vanille?")
                welkeSmaak = input("Vul hier uw antwoord in: ").upper()
                if welkeSmaak != "A" and smaak != "C" and smaak != "V":
                    HoeveelLiter = 0
                    snapNiet()
                    hoeveelLiter()
                elif welkeSmaak != "A" and smaak != "C" and smaak != "V":
                    print("")
            bonZakelijk()

        elif HoeveelLiter <= 0:
            print("Helaas verkopen wij geen hoorntjes of bakjes met minder dan 1 bolletje.")
        else:
            snapNiet()
    except ValueError:
        snapNiet()
        hoeveelLiter()

def welkom():
    global i
    global antwoord3
    print("Welkom bij Papi Gelato")
    while i == 0:
        particulierOfZakelijk = input("Bent u p) particulier of z) zakelijk? ").lower()
        if particulierOfZakelijk == "p" or particulierOfZakelijk == "particulier":
            aantalbolletjes()
        elif particulierOfZakelijk == "z" or particulierOfZakelijk == "zakelijk":
            hoeveelLiter()
        else:
            snapNiet()

welkom()