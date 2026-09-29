print("Program starting.\nWelcome to the unit converter program!\nFollow the menu instructions below.\n")
print("Options:\n1 - Length\n2 - Weight\n0 - Exit")
choice0 = int(input("Your choice: "))
#Menu 1 Length
if choice0 == 1:
    print("Length options:\n1 - Meters to kilometers\n2 - Kilometers to meters\n0 - Exit")
    #Meters to kilometers
    choice1 = int(input("Your choice: "))
    if choice1 == 1:
        mtokm = float(input("Insert meters: "))
        print(f"{mtokm} m is {round((mtokm/1000, 1))}.")
        #Kilometers to meters
    elif choice1 == 2:
        kmtom = float(input("Insert kilometers: "))
        print(f"{kmtom} km is {round((kmtom*1000))} m.")
        #Exit
    elif choice1 == 0:
        print("Exiting...")
    else:
        print("Unknown option.")    
#Menu 1 Weight
elif choice0 == 2:
    print("Length options:\n1 - Grams to pounds\n2 - Pounds to grams\n0 - Exit")
    #Grams to pounds
    choice2 = int(input("Your choice: "))
    if choice2 == 1:
        gtop = float(input("Insert grams: "))
        print(f"{gtop} g is {round((gtop/0.002205))} lb.")
    #Pounds to grams
    elif choice2 == 2:
        ptog = float(input("Insert pounds: "))
        print(f"{ptog} lb is {round((ptog*0.002205))}")
    #Exit
    elif choice2 == 0:
        print("Exiting...")
    else:
        print("Unknown option.")    
#Menu 1 Exit      
elif choice0 == 0:
    print("Exiting...") 
else:
    print("Unknown option.\n")
print("Program ending.")    
        