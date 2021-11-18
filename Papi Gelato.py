# Jurrian Schouten
# 99067235

e = 0
prijsBolletjes = 1.10
prijsHorrentjes = 1.25
prijsBakje = 0.75
hoorntje = 0
bakje = 0
totaalBolletjes = 0
toppingKosten = 0.00
aantalToppings = 0
lijstMetToppings = ["sr", "slagroom", "sp", "sprinkels", "cs", "caramelsaus"]

def sorry():
    print("Sorry, zulke grote bakken hebben we niet")

def snapNiet():
    print("Sorry, dat snap ik niet...")



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
                if antwoord3 == "bakje":
                    toppingKosten += 0.90

                elif antwoord3 == "hoorntje":
                    toppingKosten += 0.60

            else:
                snapNiet()
        else:
            snapNiet()

def bon():
    print("Bedankt en tot ziens!")
    print("---------[Papi Gelato]---------")
    print("Bolletjes" ,  totaalBolletjes, "X",  prijsBolletjes,  "= €",   float(totaalBolletjes) * prijsBolletjes)
    if hoorntje >= 1:
        print("Horrentjes",  hoorntje, "X",  prijsHorrentjes, "= €",   float(totaalBolletjes) * prijsHorrentjes)
    if bakje >= 1:
        print("Bakje"     ,  bakje, "X",  prijsBakje,      "= €",   float(totaalBolletjes) * prijsBakje)
    if aantalToppings >= 1:
        print("Topping"   ,  aantalToppings, "X", toppingKosten, "= €", float(aantalToppings) * toppingKosten)
    e = 1


print("Welkom bij Papi Gelato")


while e == 0:
    bolletjes = int(input("Hoeveel bolletjes wilt u? "))
    totaalBolletjes += bolletjes
    if bolletjes <= 3 and bolletjes >= 0:
        for i in range(1,bolletjes + 1):
            print("Welke smaak wilt u voor bolletje nummer", i, "A) Aardbei, C) Chocolade, M) Munt of V) Vanille?")
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
                    bon()
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
                    bon()
                    break
                else:
                    print("Sorry, dat snap ik niet...")
                    break
            else:
                snapNiet()
        else:
            snapNiet()
    elif bolletjes >= 3 and bolletjes <= 8:
        print("Dan krijgt u van mij een bakje met", bolletjes, "bolletjes")
        bakje += 1
        for i in range(1,bolletjes + 1):
            print("Welke smaak wilt u voor bolletje nummer", str(i), "A) Aardbei, C) Chocolade, M) Munt of V) Vanille?")
            smaak = input("Vul hier uw antwoord in: " ).upper()
        if smaak == "A" or antwoord2 == "C" or antwoord2 == "M" or antwoord2 == "V":
            topping()
            antwoord4 = input("Hier is uw bakje met "+ str(bolletjes) +" bolletje(s). Wilt u nog meer bestellen? (Y/N)").upper()
            if antwoord4 == "Y":
                print("")
            elif antwoord4 == "N":
                bon()
                e = 1
            else:
                snapNiet()
        else:
            snapNiet()

    elif bolletjes > 8:
        sorry()
    else:
        snapNiet()
