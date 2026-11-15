LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decode(Content):
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
                    break   
                elif character == UPPER_ALPHABETS[i]:
                    if i + 13 < 26:
                        i += 13
                    else:
                        i += 13 - 26
                    result += UPPER_ALPHABETS[i]
                    break      
    return result

def writeFile(filename, mode, text):
    fileHandler = open(filename, mode, encoding="UTF-8")
    fileHandler.write(text)
    fileHandler.close()

def readFile(filename):
    fileHandler = open(filename, 'r', encoding="UTF-8")
    rows = fileHandler.readlines()
    fileHandler.close()
    return rows

def main():
    print("Travel starting.")
    places = ["home", "Galba's palace", "Otho's palace", "Vitellius' palace", "Vespasian's palace"]
    progressFile = "player_progress.txt"
    savedTurn = readFile(progressFile)
    latestSave = ""
    for row in savedTurn:
        if row.strip() !="":
            latestSave = row.strip()
    savedturnData = latestSave.split(";")
    gkg_file = f"{savedturnData[1]}_{savedturnData[2]}.gkg"
    currentPlace = int(savedturnData[0])
    nextPlace = int(savedturnData[1])
    print(f"Currently at {places[currentPlace]}.")
    print(f"Travelling to {places[nextPlace]}...")
    print(f"...Arriving to the {places[nextPlace]}.")
    print("Passing the guard at the entrance.")
    passPhrase = decode(savedturnData[2])
    print(f'"{passPhrase.capitalize()}!"')
    print(f"Looking for the message in the palace...")
    print("Ah, there it is! Seems cryptic.")
    gkgrows = readFile(gkg_file)
    nextgkgrow = gkgrows[0].strip()
    writeFile(progressFile, "a", "\n" + nextgkgrow)
    print(f"[Game] Progress autosaved!")
    print("Deciphering Emperor's message...")
    cipheredMessage = ""
    for line in gkgrows[1:]:
        cipheredMessage +=line
    decodedMessage = decode(cipheredMessage)
    decodedFile = f"{savedturnData[1]}-{passPhrase}.txt"
    writeFile(decodedFile, "w", decodedMessage)    
    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")

if __name__ == "__main__":
    main()

