def Options():
    print("\nOptions:\n1 - Show count\n2 - Increase count\n3 - Reset count\n0 - Exit")
    return None

def askChoice():
    while True:
        choice = input("Your choice: ")
        if choice.isnumeric() and int(choice) in range(0,4):
            return int(choice)
        else:
            print("Unknown option!")

def showCount(count):
    print(f"Current count - {count}")

def increaseCount(count):
    return count + 1

def resetCount(): 
    return 0             

def main():
    print("Program starting.")
    count = 0
    while True:
        Options()
        choice = askChoice()
        if choice == 1:
            showCount(count)    
        elif choice == 2: 
            count = increaseCount(count)
            print(f"Count increased!")
        elif choice == 3: 
            count = resetCount()
            print("Cleared count!")
        elif choice == 0: 
            print("Exiting program.")
            break

    print("\nProgram ending.")

main()