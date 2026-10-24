delimiter = ","

def collectWords():
    string = input("Insert word(empty stops): ")
    while True:
        PWord = input("Insert word(empty stops): ")
        if len(PWord) == 0:
            break
        string = string + delimiter + PWord
    return string
       

def analyseWords(PWord):     
    all_words = PWord.split(delimiter)
    word_amount = len(all_words)
    characters = len(PWord.replace(delimiter, ""))
    Avg = characters / word_amount
    print(f"- {word_amount} Words")
    print(f"- {characters} Characters")
    print("- {:.2f} Average word length".format(Avg))
    return None

def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)

    print("\nProgram ending.")

main()