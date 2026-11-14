LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def saveText(saveFile, cipheredText):
    fileHandler = open(saveFile, 'w', encoding="UTF-8")
    fileHandler.write(cipheredText)
    fileHandler.close()
    return None

def cipherText(Content):
    result = ""
    for character in Content:
        if character not in LOWER_ALPHABETS and character not in UPPER_ALPHABETS:
            result += character
        else:    
            for i in range(26):
                if character == LOWER_ALPHABETS[i]:
                    if i + 13 < 26:
                        i += 13
                    else:
                        i += 13 - 26
                    result += LOWER_ALPHABETS[i]   
                elif character == UPPER_ALPHABETS[i]:
                        if i + 13 < 26:
                            i += 13
                        else:
                            i += 13 - 26
                        result += UPPER_ALPHABETS[i]      
    return result

def collectText():
    Content = ""
    while True:
        text = input("Insert row(empty stops): ")
        if text == "":
            break
        else:
            Content +=text + "\n"
    return Content

def main():
    print("Program starting.")
    print("")
    print("Collecting plain text rows for ciphering.")
    collectedText = collectText()
    print("#### Ciphered text ####")
    cipheredText = cipherText(collectedText)
    print(cipheredText)
    print("#### Ciphered text ####")
    saveFile = input("Insert filename to save: ")
    saveText(saveFile, cipheredText)
    print("Ciphered text saved!")
    print("Program ending.")

main()