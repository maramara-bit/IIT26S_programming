def readFile(sourceFile):
    fileHandler = open(sourceFile, 'r', encoding="UTF-8")
    Content = ''
    row = fileHandler.readline()
    #Reads a line, moves to next, while loop works until row is empty  
    while row != '':
        Content += row
        #Same as content = content + row
        row = fileHandler.readline()
    fileHandler.close()
    return Content

def writeFile(destinationFile, Content):
    fileHandler = open(destinationFile, 'w', encoding="UTF-8")
    fileHandler.write(Content)
    fileHandler.close()
    return None

def main():
    print("Program starting.")
    print("This program can copy a file.")
    sourceFile = input("Insert source filename: ")
    destinationFile = input("Insert destination filename: ")
    print(f"Reading file '{sourceFile}' content.")
    copyFile = readFile(sourceFile)
    print("File content ready in memory.")
    print(f"Writing content into file '{destinationFile}'.")
    writeFile(destinationFile, copyFile)
    print("Copying operation complete.")
    print("Program ending.")

main()