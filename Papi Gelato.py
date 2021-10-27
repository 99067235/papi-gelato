# Jurrian Schouten
# 99067235

e = 0

def bakjeKiezen():
    antwoord = input("Wilt u deze {antwoord} bolletje(s) in A) een hoorntje of B) een bakje? ")

def sorry():
    print("Sorry, zulke grote bakken hebben we niet")
    
print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")

while e == 0:
    antwoord = int(input("Hoeveel bolletjes wilt u? "))
    if antwoord <= 3 and antwoord >= 0:
        bakjeKiezen()
        break
    else:
        sorry()
