def insertWord():
    Word = input("Insert word: ")
    return Word

def showWord(PWord):
    print(f'Current word - "{PWord}".')

def reverseWord(PWord):
    revWord = PWord[::-1]
    print(f'Word reversed - "{revWord}".')


def main():
    print("Program starting.")
    Word = ""
    while True:
        print("\nOptions:\n1 - Insert word\n2 - Show current word\n3 - Show current word in reverse\n0 - Exit")
        choice = int(input("Your choice: "))
        if choice == 1: 
            Word = insertWord()
        elif choice == 2: 
            showWord(Word)
        elif choice == 3: 
            reverseWord(Word)
        elif choice == 0: 
            print("Exiting program.")
            break
        else: print("Unknown option! Try again.") 
    print("\nProgram ending.")

main()