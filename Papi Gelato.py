# Jurrian Schouten
# 99067235

e = 0
prijsBolletjes = 1.10
prijsHorrentjes = 1.25
prijsBakje = 0.75
hoorntje = 0
bakje = 0
BestaandeSmaken = ["aardbei", "a", "chocolade", "c", "munt", "m" "vanille", "v"]
ReturnsInLoop = 0

def WrongAnswer():
    print("Dit is fout")

def sorry():
    print("Sorry, zulke grote bakken hebben we niet")

def snapNiet():
    print("Sorry, dat snap ik niet...")



print("Welkom bij Papi Gelato")


while e == 0:
    antwoord = int(input("Hoeveel bolletjes wilt u? "))
    if antwoord <= 3 and antwoord >= 0:
        for i in range(1,antwoord + 1):
            print("Welke smaak wilt u voor bolletje nummer", i, "A) Aardbei, C) Chocolade, M) Munt of V) Vanille?")
            antwoord2 = input("Vul hier uw antwoord in: " ).upper()
        if antwoord2 == "A" or antwoord2 == "C" or antwoord2 == "M" or antwoord2 == "V":
            antwoord3 = input("Wilt u deze "+ str(antwoord) +" bolletje(s) in A) een hoorntje of B) een bakje? ").upper()
            if antwoord3 == "A":
                hoorntje += 1
                antwoord4 = input("Hier is uw hoorntje met "+ str(antwoord) +" bolletje(s). Wilt u nog meer bestellen? (Y/N)").upper()
                if antwoord4 == "Y":
                    print("")
                elif antwoord4 == "N":
                    print("Bedankt en tot ziens!")
                    print("---------[Papi Gelato]---------")
                    print("Bolletjes" ,  antwoord, "X",  prijsBolletjes,  "= €",   float(antwoord) * prijsBolletjes)
                    if hoorntje >= 1:
                        print("Horrentjes",  antwoord, "X",  prijsHorrentjes, "= €",   float(antwoord) * prijsHorrentjes)
                    if bakje >= 1:
                        print("Bakje"     ,  antwoord, "X",  prijsBakje,      "= €",   float(antwoord) * prijsBakje)
                    e = 1
                    break
                else:
                    snapNiet()
            elif antwoord3 == "B":
                bakje += 1
                antwoord4 = input("Hier is uw bakje met "+ str(antwoord) +" bolletje(s). Wilt u nog meer bestellen? (Y/N)").upper()
                if antwoord4 == "Y":
                    print("")
                elif antwoord4 == "N":
                    print("Bedankt en tot ziens!")
                    print("---------[Papi Gelato]---------")
                    print("Bolletjes" ,  antwoord, "X",  prijsBolletjes,  "= €",   antwoord * prijsBolletjes)
                    if hoorntje >= 1:
                        print("Horrentjes",  antwoord, "X",  prijsHorrentjes, "= €",   antwoord * prijsHorrentjes)
                    if bakje >= 1:
                        print("Bakje"     ,  antwoord, "X",  prijsBakje,      "= €",   antwoord * prijsBakje)
                    e = 1
                    break
                        
                else:
                    print("Sorry, dat snap ik niet...")
                    break
            else:
                sorry()
        else:
            sorry()
    elif antwoord >= 3 and antwoord <= 8:
        print("Dan krijgt u van mij een bakje met", antwoord, "bolletjes")
        bakje += 1
        while ReturnsInLoop != antwoord + 1:
            print("Welke smaak wilt u voor bolletje nummer", str(ReturnsInLoop), "A) Aardbei, C) Chocolade, M) Munt of V) Vanille?")
            smaak = input("Vul hier uw antwoord in: " )
            if smaak in BestaandeSmaken:
                ReturnsInLoop += 1
                antwoord3 = input("Wilt u deze "+ str(antwoord) +" bolletje(s) in A) een hoorntje of B) een bakje? ").upper()
                if antwoord3 == "A":
                    hoorntje += 1
                    antwoord4 = input("Hier is uw hoorntje met "+ str(antwoord) +" bolletje(s). Wilt u nog meer bestellen? (Y/N)").upper()
                    if antwoord4 == "Y":
                        print("")
                    elif antwoord4 == "N":
                        print("Bedankt en tot ziens!")
                        print("---------[Papi Gelato]---------")
                        print("Bolletjes" ,  antwoord, "X",  prijsBolletjes,  "= €",   float(antwoord) * prijsBolletjes)
                        if hoorntje >= 1:
                            print("Horrentjes",  antwoord, "X",  prijsHorrentjes, "= €",   float(antwoord) * prijsHorrentjes)
                        if bakje >= 1:
                            print("Bakje"     ,  antwoord, "X",  prijsBakje,      "= €",   float(antwoord) * prijsBakje)
                        e = 1
                        break
                    
            else:
                snapNiet()
                
        antwoord4 = input("Wilt u nog meer bestellen? (Y/N)").upper()
        if antwoord4 == "Y":
            print("")
        elif antwoord4 == "N":
            print("Bedankt en tot ziens!")
            print("---------[Papi Gelato]---------")
            print("Bolletjes" ,  antwoord, "X",  prijsBolletjes,  "= €",   antwoord * prijsBolletjes)
            if hoorntje >= 1:
                print("Horrentjes",  antwoord, "X",  prijsHorrentjes, "= €",   antwoord * prijsHorrentjes)
            if bakje >= 1:
                print("Bakje"     ,  antwoord, "X",  prijsBakje,      "= €",   antwoord * prijsBakje)
            e = 1
            break
        else:
            snapNiet()
            
                
    elif antwoord > 8:
        sorry()
    else:
        snapNiet()
