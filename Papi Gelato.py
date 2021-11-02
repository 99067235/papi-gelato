# Jurrian Schouten
# 99067235

e = 0

def sorry():
    print("Sorry, zulke grote bakken hebben we niet")

print("Welkom bij Papi Gelato")


while e == 0:
    antwoord = int(input("Hoeveel bolletjes wilt u? "))
    if antwoord <= 3 and antwoord >= 0:
        for i in range(1,antwoord + 1):
            print("Welke smaak wilt u voor bolletje nummer", i, "A) Aardbei, C) Chocolade, M) Munt of V) Vanille?")
            antwoord2 = input("Vul hier uw antwoord in: " ).upper()
        if antwoord2 == "A" or "C" or "M"  "V":
            antwoord3 = input("Wilt u deze "+ str(antwoord) +" bolletje(s) in A) een hoorntje of B) een bakje? ").upper()
            if antwoord3 == "A" or "B":
                antwoord4 = input("Hier is uw hoorntje/bakje met "+ str(antwoord) +" bolletje(s). Wilt u nog meer bestellen? (Y/N)").upper()
                if antwoord4 == "Y":
                    print("")
                elif antwoord4 == "N":
                    print("Bedankt en tot ziens!")
                    break
                else:
                    print("Sorry, dat snap ik niet...")
                    break
            else:
                sorry() 
        else:
            sorry()
    else:
        sorry()

    

