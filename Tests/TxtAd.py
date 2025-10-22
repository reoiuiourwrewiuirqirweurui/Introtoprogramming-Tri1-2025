def JoeMoma():
    print("Yeah, this is self explanatory. YOu have Options to make")
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
def Killed():
    print("Yeah, You Died")
    return("Bad Ending Acheived!")
def Stolen():
    print("You Stole Some stuff!")
    Scene2 = input("Dialog W.I.P")
    if Scene2 == "1":
        print("W.I.P")
    elif Scene2 == "3":
        print("W.I.P")
    
    if Scene2 == "1":
        print("WIP2")
    elif Scene2 == "4":
        print("wipLOL")
    
def GoForest():
    print("You walked into the forest unknownenly that the Town was massacred.")
    Fowoest = input(">")
    if Fowoest == "1":
        print("WIP")
#Mr. osowski Making me want to cry on the floor 😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭
