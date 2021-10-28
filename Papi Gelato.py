# Jurrian Schouten
# 99067235

e = 0

def sorry():
    print("Sorry, zulke grote bakken hebben we niet")

print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")


while e == 0:
    antwoord = int(input("Hoeveel bolletjes wilt u? "))
    if antwoord <= 3 and antwoord >= 0:
        antwoord2 = input("Wilt u deze "+ str(antwoord) +" bolletje(s) in A) een hoorntje of B) een bakje? ").upper()
        if antwoord2 == "A" or "B":
            antwoord3 = input("Hier is uw hoorntje/bakje met "+ str(antwoord) +" bolletje(s). Wilt u nog meer bestellen? (Y/N)").upper()
            if antwoord3 == "Y":
                print("")
            elif antwoord3 == "N":
                print("Bedankt en tot ziens!")
                break
            else:
                print("Sorry, dat snap ik niet...")
                break
        else:
            sorry() 
    else:
        sorry()
