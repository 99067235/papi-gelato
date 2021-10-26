# Jurrian Schouten
# 99067235
kiezen = False

def bakjeKiezen():
    antwoord = input("Wilt u deze {antwoord} bolletje(s) in A) een hoorntje of B) een bakje? ")
    
    if antwoord == "A" or "B":
        kiezen = True
    else:
        kiezen = False

while kiezen == False:
    antwoord = input("Wilt u deze {antwoord} bolletje(s) in A) een hoorntje of B) een bakje? ")
    
    if antwoord == "A" or "B":
        kiezen = True
    else:
        kiezen = False
    


def sorry():
    print("Sorry, zulke grote bakken hebben we niet")

print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")

antwoord = int(input("Hoeveel bolletjes wilt u? "))
if antwoord <= 3 and antwoord >= 0:
    bakjeKiezen()
else:
    sorry()
