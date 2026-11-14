def analyseNumbers(contentFile):
    numberList = contentFile.split(';')
    total = 0
    count = 0
    greatest = 0
    average = 0
    for i in numberList:
        number = int(i)
        total += number
        count +=1
        if number > greatest:
            greatest = number
    average = f"{total/count:.2f}"
    return f"{count};{total};{greatest};{average}"  

def readFile(sourceFile):
    fileHandler = open(sourceFile, 'r', encoding="UTF-8")
    values: str = ""
    row = fileHandler.readline()
    while row != '':
        value = row.strip()
        if value != '':
            if values == '':
                values += value
            else:
                values += ";" + value   
        row = fileHandler.readline()
    fileHandler.close()
    return values

def main():
    print("Program starting.")
    sourceFile = input("Insert filename: ")
    contentFile = readFile(sourceFile)
    numberAnalysis = analyseNumbers(contentFile)
    print("#### Number analysis - START ####")
    print(f'File "{sourceFile}" results:')
    print("Count;Sum;Greatest;Average")
    print(f"{numberAnalysis}")
    print("#### Number analysis - END ####")
    print("Program ending.")

main()