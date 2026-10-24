def frameWord(PWord):
#Prints as many * as there is chars in word. 
#PWord is word renamed, parameter word.
    print("\n")
    print("*" * (len(PWord) +4))
    print(f"* {PWord} *")
    print("*" * (len(PWord) + 4))
    return None

def main():
    print("Program starting.")
    word = input("Insert a word: ")
#Calling frameword in main, skips and moves to frameword, sends word to frameword 
    frameWord(word)
    print("\nProgram ending.")
    return None

#Only line operating when starting
main()
#def defines a function