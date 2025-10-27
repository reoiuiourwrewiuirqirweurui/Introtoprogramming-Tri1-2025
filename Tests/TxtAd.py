def JoeMoma():
    print("Yeah, this is self explanatory. YOu have Options to make ")
    print("1. Go to Town")
    print("2. Go to the Forest.")
    choice = input(">")
    if choice == "1":
        GoTown()
    elif choice == "2":
        GoForest()
    else:
        print("Try Again!")
        JoeMoma()
def GoTown():
    print("You see blood every where")
    print("1. Find the person who caused this.")
    print("2. Steal Items so you can have something to defend yourself.")
    Scene1 = input(">")
    if Scene1 == "1":
        Killed()
    elif Scene1 == "2":
        Stolen()
    else:
        print("Uhhh why?")
    GoTown()
def Killed():
    print("Yeah, You Died")
    return("Bad Ending Acheived!")
def Stolen():
    print("You Stole Some stuff! YOU HAVE MORE OPTIONS")
    print("1. Fight the Monster")
    print("2. Skip to the ending")
    print("3. Escape to somewhere else")
    Scene2 = input(">")
    if Scene2 == "1":
        NeutralEnding()
    else:
        print("Error!")
    
    if Scene2 == "2":
        TheVoidEnding()
    elif Scene2 == "4":
        LocatedLake()
    else:
        print("error")
    
def GoForest():
    print("You walked into the forest unknownenly that the Town was massacred.")
    Fowoest = input(">")
    if Fowoest == "1":
        print("WIP")
def NeutralEnding():
    print("You're fighting a monster.")
    print("1. Attack the monster with your strength.")
    print("2. Outsmart the DreamMonster")
    Monster = input(">")
    if Monster == "1":
        Neutrality()
    elif Monster == "2":
        ItsADreamEnding()
def Neutrality():
    print("You Killed the Monster but you're alone with no one alive...")
    return("Neutral ending acheived!")
    #Neutral Ending Acheived!
def ItsADreamEnding():
    print("It's All fake?????")
    return("You got the dream ending!")
    #Yeah It's the Dream ending
def LocatedLake():
    print(" You ran to the Lake..")
    print("1. Explore The Area.")
    print("2.Escape the area so you won't be in danger")
    Lake = input(">")
    if Lake == "1":
        Exploration()
    elif Lake == "2":
        Escape()
    else:
        return("Error!")
def Exploration():
    print("You Found a Secret Potion!")
    print("1. Fight the Monster Now")
    print("2. Drink the potion.")
    print("3. *Gets Transported to somewhere else.* ")
    Explore = input(">")
    if Explore == "1":
        CoolEnding()
    elif Explore == "2":
        RealityEnding()
    else:
        return("Error!")
    if Explore == "3":
        GensokyoEnding()
    else:
        return("Error!")
def CoolEnding():
    print("Nice you won against them by poisoning the monster without any help!")
    #They Used a potion against them
def RealityEnding():
    print("You drank the potion and found yourself in front of your own house. you're in your actual world")
    #This is different from the 'Dream ending' as in the person is trapped in the world vs the person dreaming about it
    return("Reality ending acheived!")
def GensokyoEnding():
    print("You touched the potion and find your self at the Fantasy land. You see a shrine named 'The Hakurei Shine'")
    #This is similar to the Reality ending except it's real and They're being transported to Gensokyo after touching the potion
    return("You got the Gensokyo Ending!")
def TheVoidEnding():
    print("You skipped to the ending but this one is unfinished.")
    return("Void Ending! Try again!")







    



#Mr. osowski Making me want to cry on the floor 😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭
