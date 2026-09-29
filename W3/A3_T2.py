print("Program starting.\nString comparisons.")
word1 = input("Insert first word: ").lower()
char1 = input("Insert a character: ").lower()
if len(word1.split(char1)) > 1:
    print(f"Word \"{word1}\" contains character \"{char1}\".")
else:
    print(f"Word {word1} doesn't contain character {char1}.")
word2 = input("Insert second word: ").lower()
if word2 < word1:
     print(f"The second word \"{word2}\" is before the first word \"{word1}\" alphabetically.")
elif word2 > word1:
     print(f"The first word \"{word1}\" is before the second word \"{word2}\", alphabetically.")
elif word2 == word1:
      print(f"Both words are the same alphabetically, \"{word1}\".")
print("Program ending.")