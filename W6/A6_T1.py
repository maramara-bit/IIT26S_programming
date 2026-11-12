#Returning a variable in string format
def readFile(Filename: str) -> str:
    Filehandler = open(Filename, 'r', encoding="UTF-8")
    Content = ''
    Row = Filehandler.readline()
#Reads a line, moves to next, while loop works until row is empty  
    while Row != '':
        Content += Row
        #Same as content = content + row
        Row = Filehandler.readline()
    Filehandler.close()
    return Content

def main():
    print("Program starting.")
    print("This program can read a file.")
    Filename = input("Insert filename: ")
    fileContent = readFile(Filename)
    print(f"#### START {Filename} ####")
    print(fileContent)
    print(f"#### END {Filename} ####")
    print("Program ending.")
    return None

main()