def readFile(PFilename: str, PRows: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PRows.clear()
    filehandle = open(PFilename, 'r', encoding="UTF-8")
    firstrow = filehandle.readline()
    for line in filehandle:
        if line != "\n":
            PRows.append(line.rstrip("\n"))
    filehandle.close()
    return None

WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)

def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    WeekdayTimestampAmount: list[int] = [0, 0, 0, 0, 0, 0, 0]
    for i in PRows:
        columns = i.split(";")
        for j in range(len(WEEKDAYS)):
            if columns[0] == WEEKDAYS[j]:
                WeekdayTimestampAmount[j] += 1
    for i in range(len(WEEKDAYS)):
        PResults.append(f" - {WEEKDAYS[i]} {WeekdayTimestampAmount[i]} stamps")
    WeekdayTimestampAmount.clear()
    return None

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for result in PResults:
        print(result)
    print("### Timestamp analysis ###")
    return None

def main() -> None:
    print("Program starting.")
    rows: list[str] = []
    results: list[str] = []
    filename = input("Insert filename: ")
    readFile(filename, rows)
    analyseTimestamps(rows, results)
    displayResults(results)
    rows.clear()
    results.clear()
    print("Program ending.")
    return None

if __name__=="__main__":
    main()