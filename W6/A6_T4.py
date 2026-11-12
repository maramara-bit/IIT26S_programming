def analyzeFile(contentFile):
    nameList = contentFile.split(';')
    nameCount = len(nameList)
    characterCount = 0
    shortName = len(nameList[0])
    longName = len(nameList[0])
    for name in nameList:
        currentnameL = len(name)
        characterCount += currentnameL
        if currentnameL < shortName:
            shortName = currentnameL
        if currentnameL > longName:
            longName = currentnameL
    average = characterCount/nameCount
    return nameCount, shortName, longName, average          

def readFile(sourceFile):
    fileHandler = open(sourceFile, 'r', encoding="UTF-8")
    Content = ''
    row = fileHandler.readline()
    while row != '':
        strippedRow = row.strip()
        if strippedRow != '':
            if Content == '':
                Content += strippedRow
            else:
                Content += ";" + strippedRow   
        row = fileHandler.readline()
    fileHandler.close()
    return Content

def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    sourceFile = input("Insert filename to read: ")
    print(f'Reading names from "{sourceFile}".')
    contentFile = readFile(sourceFile)
    print("Analysing names...")
    nameCount, shortName, longName, average = analyzeFile(contentFile)
    print("Analysis complete!")
    print("#### REPORT BEGIN ####")
    print(f"Name count - {nameCount}")
    print(f"Shortest name - {shortName} chars")
    print(f"Longest name - {longName} chars")
    print(f"Average name - {average:.2f} chars")
    print("#### REPORT END ####")
    print("Program ending.")

main()