Touhou15 = input("WHo's the extra boss of TH15?\n")
Owen = input("who is Owen Rossing?\n")
Touhou14 = input("What's the best shottype?\n")
MrOsowski = input("who is the teacher of this class?\n")
dwpk = input("what do you mean?\n")
def score():
    score = 0
    if Touhou15 == "Hecatia":
        score = score + 1
    if Owen == "Guy in class":
        score = score + 1
    if Touhou14 == "MarisaB":
        score = score + 1
    if MrOsowski == "Mr. Osowski":
        score = score + 1
    if dwpk == "Oh oh oh":
        score = score + 1
    print("Score: " + str(score) + "/5")

score()
        