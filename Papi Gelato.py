from pickle import TRUE

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
lijstmetBesteldeSmaken = []
gekozenbakje = False
a = True

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
    my_formatter = "{0:.2f}"
    print("Bedankt en tot ziens!")
    print("---------[Papi Gelato]---------")
    #formatteren kosten bolletjes
    kostenBolletjes = float(totaalBolletjes * prijsBolletjes)
    formatted_PrijsBolletjes = float(totaalBolletjes) * prijsBolletjes
    bonPrijsBolletjes = my_formatter.format(formatted_PrijsBolletjes)
    print("Bolletjes:   "  ,  totaalBolletjes, "X",  prijsBolletjes,  "= €",   bonPrijsBolletjes)
    #formatteren kosten hoorntje
    kostenHoorntje = hoorntje * prijsHorrentjes
    BonprijsHoorntje = my_formatter.format(kostenHoorntje)
    if hoorntje >= 1:
        print("Horrentjes:  ",  hoorntje, "X",  prijsHorrentjes, "= €",   BonprijsHoorntje)
    #formatteren kosten bakje
    kostenBakje = bakje * prijsBakje
    BonprijsBakje = my_formatter.format(kostenBakje)
    if bakje >= 1:
        print("Bakje:       "     ,  bakje, "X",  prijsBakje,      "= €",   BonprijsBakje)
    #formatteren prijs toppings
    BonPrijsToppings = my_formatter.format(toppingKosten)
    if aantalToppings >= 1:
        kostenToppings = float(aantalToppings) * toppingKosten
        print("Topping:     "   ,  aantalToppings, "X", toppingKosten, "= €", BonPrijsToppings)
    print("             ---------------- +")
    formatted_total = kostenBolletjes + kostenHoorntje + kostenBakje + kostenToppings
    total = my_formatter.format(formatted_total)
    print("Totaal       = €",total)
    exit()

def bonZakelijk():
    global HoeveelLiter
    global i
    my_formatter = "{0:.2f}"
    prijs = HoeveelLiterkeuze * 9.80
    btw = prijs / 100 * 9
    btwprijs = round(float(prijs/100 * Btw),2)
    #formatteren totaal
    formatted_prijsZakelijk = my_formatter.format(prijs)
    #formatteren btw
    formatted_btw = my_formatter.format(btwprijs)
    berekeningBtw = round(float(formatted_prijsZakelijk)) / 100 * 9
    print("Bedankt en tot ziens!")
    print("---------[Papi Gelato]---------")
    print("Liter:  ", HoeveelLiterkeuze, "X €","9,80", " = €", formatted_prijsZakelijk)
    print("             ---------------- +")
    print("Totaal               = €", formatted_prijsZakelijk)
    print("BTW (9%)             = €", berekeningBtw)
    exit()

def bakjeGekozen(bolletjes):
    global bakje
    bakje += 1
    topping(bolletjes)
    antwoord4 = input("Hier is uw bakje met "+ str(bolletjes) +" bolletje(s). Wilt u nog meer bestellen? (Y/N)").upper()
    if antwoord4 == "Y":
        print("")
        aantalbolletjes()
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
        aantalbolletjes()
    elif antwoord4 == "N":
        bonParticulier()
    else:
        snapNiet()
        hoorntjeMeerbestellen(bolletjes)

def keuzeVerpakking(bolletjes):
    global hoorntje
    global antwoord3
    global bakje
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
    roundsLoop = 1
    while roundsLoop != bolletjes + 1:
        print("Welke smaak wilt u voor bolletje nummer", str(roundsLoop), "A) Aardbei, C) Chocolade, of V) Vanille?")
        smaak = input("Vul hier uw antwoord in: " ).upper()
        if smaak == "A" or smaak == "C" or smaak == "M" or smaak == "V":
            roundsLoop += 1
        else:
            snapNiet()
    keuzeVerpakking(bolletjes)

def bakjeMeerBestellen(bolletjes):
    global antwoord3
    global a
    topping(bolletjes)
    while a == True:
        antwoord4 = input("Hier is uw bakje met "+ str(bolletjes) +" bolletje(s). Wilt u nog meer bestellen? (Y/N)").upper()
        if antwoord4 == "Y":
            a = False
            print("")
            aantalbolletjes()
        elif antwoord4 == "N":
            a = False
            bonParticulier()
            exit()
        else:
            snapNiet()
            a = True

def welkeSmaakGroot(bolletjes):
    global bakje
    global smaak
    global antwoord3
    roundsLoop = 1
    while roundsLoop != bolletjes + 1:
        print("Welke smaak wilt u voor bolletje nummer", str(roundsLoop), "A) Aardbei, C) Chocolade, of V) Vanille?")
        smaak = input("Vul hier uw antwoord in: " ).upper()
        if smaak == "A" or smaak == "C" or smaak == "M" or smaak == "V":
            roundsLoop += 1
        else:
            snapNiet()
    bakjeMeerBestellen(bolletjes)

def aantalbolletjes():
    global totaalBolletjes
    global antwoord3
    global bakje
    global kostenBakje
    try:
        bolletjes = int(input("Hoeveel bolletjes wilt u? "))
        if bolletjes <= 3 and bolletjes >= 0:
            totaalBolletjes += bolletjes
            welkeSmaak(bolletjes)
        elif bolletjes > 3 and bolletjes <= 8:
            totaalBolletjes += bolletjes
            print("Dan krijgt u van mij een bakje met", bolletjes, "bolletjes")
            bakje += 1
            antwoord3 = "B"
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


def litersIjs():
    global HoeveelLiterkeuze
    roundsLoop = 1
    HoeveelLiterkeuze = int(input("Hoeveel liter ijs wilt u bestellen? "))
    if HoeveelLiterkeuze >= 1:
        while roundsLoop != HoeveelLiterkeuze + 1:
            print("Welke smaak wilt u voor liter", str(roundsLoop), "A) Aardbei, C) Chocolade, of V) Vanille?")
            welkeSmaak = input("Vul hier uw antwoord in: ").upper()
            if welkeSmaak == "A" or welkeSmaak == "C" or welkeSmaak == "M" or welkeSmaak == "V":
                roundsLoop += 1
            else:
                snapNiet()
        bonZakelijk()
    elif HoeveelLiterkeuze <= 0:
        print("Helaas verkopen wij geen lege bakken ijs...")
    else:
        snapNiet()
    
def welkom():
    global i
    global antwoord3
    print("Welkom bij Papi Gelato")
    while i == 0:
        particulierOfZakelijk = input("Bent u p) particulier of z) zakelijk? ").lower()
        if particulierOfZakelijk == "p" or particulierOfZakelijk == "particulier":
            aantalbolletjes()
        elif particulierOfZakelijk == "z" or particulierOfZakelijk == "zakelijk":
            litersIjs()
        else:
            snapNiet()

welkom()