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

def sorry():
    print("Sorry, zulke grote bakken hebben we niet")

def snapNiet():
    print("Sorry, dat is geen optie die we aanbieden...")



def topping():
        global aantalToppings
        global toppingKosten
    
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

def bonParticulier():
    global kostenBakje
    global kostenToppings
    global kostenHoorntje
    global kostenBolletjes
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
    e = 1

def bonZakelijk():
    global HoeveelLiter
    prijs = HoeveelLiter * 9.80
    btw = prijs / 100 * 6
    print("Bedankt en tot ziens!")
    print("---------[Papi Gelato]---------")
    print("Liter:  ", HoeveelLiter, "X €","9,80", " = €", prijs)
    print("             -------------- +")
    print("Totaal               = €", prijs)
    print("BTW (6%)             = €", btw)

def test():
    global bakje
    print("Dan krijgt u van mij een bakje met", bolletjes, "bolletjes")
    bakje += 1
    for i in range(1,bolletjes + 1):
        print("Welke smaak wilt u voor bolletje nummer", str(i), "A) Aardbei, C) Chocolade, of V) Vanille?")
        smaak = input("Vul hier uw antwoord in: " ).upper()
    if smaak == "A" or smaak == "C" or smaak == "M" or smaak == "V":
        topping()
        antwoord4 = input("Hier is uw bakje met "+ str(bolletjes) +" bolletje(s). Wilt u nog meer bestellen? (Y/N)").upper()
        if antwoord4 == "Y":
            print("")
        elif antwoord4 == "N":
            bonParticulier()
            e = 1
        else:
            snapNiet()
    else:
        snapNiet()


print("Welkom bij Papi Gelato")
while i == 0:
    particulierOfZakelijk = int(input("Bent u 1) particulier of 2) zakelijk? "))
    if particulierOfZakelijk == 1:
        while e == 0:
            bolletjes = int(input("Hoeveel bolletjes wilt u? "))
            totaalBolletjes += bolletjes
            if bolletjes <= 3 and bolletjes >= 0:
                for i in range(1,bolletjes + 1):
                    print("Welke smaak wilt u voor bolletje nummer", i, "A) Aardbei, C) Chocolade, of V) Vanille?")
                    antwoord2 = input("Vul hier uw antwoord in: " ).upper()
                if antwoord2 == "A" or antwoord2 == "C" or antwoord2 == "M" or antwoord2 == "V":
                    antwoord3 = input("Wilt u deze "+ str(bolletjes) +" bolletje(s) in A) een hoorntje of B) een bakje? ").upper()
                    if antwoord3 == "A":
                        hoorntje += 1
                        topping()
                        antwoord4 = input("Hier is uw hoorntje met "+ str(bolletjes) +" bolletje(s). Wilt u nog meer bestellen? (Y/N)").upper()
                        if antwoord4 == "Y":
                            print("")
                        elif antwoord4 == "N":
                            bonParticulier()
                            break
                        else:
                            snapNiet()
                    elif antwoord3 == "B":
                        bakje += 1
                        topping()
                        antwoord4 = input("Hier is uw bakje met "+ str(bolletjes) +" bolletje(s). Wilt u nog meer bestellen? (Y/N)").upper()
                        if antwoord4 == "Y":
                            print("")
                        elif antwoord4 == "N":
                            bonParticulier()
                            break
                        else:
                            sorry()
                            break
                    else:
                        snapNiet()
                else:
                    snapNiet()
            elif bolletjes >= 3 and bolletjes <= 8:
                print("Dan krijgt u van mij een bakje met", bolletjes, "bolletjes")
                bakje += 1
                for i in range(1,bolletjes + 1):
                    print("Welke smaak wilt u voor bolletje nummer", str(i), "A) Aardbei, C) Chocolade, of V) Vanille?")
                    smaak = input("Vul hier uw antwoord in: " ).upper()
                if smaak == "A" or smaak == "C" or smaak == "M" or smaak == "V":
                    topping()
                    antwoord4 = input("Hier is uw bakje met "+ str(bolletjes) +" bolletje(s). Wilt u nog meer bestellen? (Y/N)").upper()
                    if antwoord4 == "Y":
                        print("")
                    elif antwoord4 == "N":
                        bonParticulier()
                        e = 1
                    else:
                        snapNiet()
                else:
                    snapNiet()
            elif bolletjes <= 0:
                print("U snapt dus niet dat minder bolletjes dan 1 kopen niet kan.")
                time.sleep(1)
                print("Doe anders meteen de IQ test:")
                time.sleep(2)
                webbrowser.open("www.iqtestacademy.org")
                break
            elif bolletjes > 8:
                sorry()
            else:
                snapNiet()

    elif particulierOfZakelijk == 2:
        HoeveelLiter = int(input("Hoeveel liter ijs wilt u bestellen? "))
        if HoeveelLiter >= 1:
            for f in range(1, HoeveelLiter + 1):
                print("Welke smaak wilt u voor liter", (f), "A) Aardbei, C) Chocolade, of V) Vanille?")
                welkeSmaak = input("Vul hier uw antwoord in: ").upper()
            if welkeSmaak == "A" or welkeSmaak == "C" or welkeSmaak == "M" or welkeSmaak == "V":
                bonZakelijk()
                break
            else:
                snapNiet()
        elif HoeveelLiter <= 0:
            print("U snapt dus niet dat minder bolletjes dan 1 kopen niet kan.")
            time.sleep(1)
            print("Doe anders meteen de IQ test:")
            time.sleep(2)
            webbrowser.open("www.iqtestacademy.org")
            break
        else:
            snapNiet()
    else:
        snapNiet()