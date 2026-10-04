print("Program starting.")
wname = input("This is a program with simple menu, where you can choose which operation the program performs. Before the menu, please insert your name: ")
print("\n")
print("Options:\n1 - Print welcome message\n0 - Exit")
choice = int(input("Your choice: "))
if choice == 1:
    print(f"Welcome {wname}!")
elif choice == 0:
    print("Exiting...")
else:
    print("Unknown choice.")
print("\n")
print("Program ending.")