
def writeFile(fileName: str, content: str):
    fileHandler = open(fileName, 'w', encoding="UTF-8")
    fileHandler.write(content)
    fileHandler.close
    return None

def main() -> None:
    print("Program starting.")
    firstName = input("Insert first name: ")
    lastName = input("Insert last name: ")
    content = "{}\n{}\n".format(firstName, lastName)
    fileName = input("Insert filename: ")
    writeFile(fileName, content)
    print("Program ending.")
    return None

main()
