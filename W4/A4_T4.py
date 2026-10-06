print("Program starting.\n")
word_n = 0
char_n = 0
while True:
    word = input("Insert word (empty stops): ")
    if word == "" or word == " ":
        break
    word_n += 1
    char_n += len(word)
print(f"You inserted\n- {word_n} words\n- {char_n} characters\n")
print("Program ending.")