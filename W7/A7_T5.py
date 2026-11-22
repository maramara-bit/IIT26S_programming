class TIMESTAMP:
    weekday: str = ""
    hour: str = ""
    consumption: float = 0.0
    price: float = 0.0

class DAY_USAGE:
    weekday: str = ""
    usage: float = 0.0
    cost: float = 0.0    

def readFile(PFilename: str, PTimestamps: list[TIMESTAMP]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PTimestamps.clear()
    filehandle = open(PFilename, 'r', encoding="UTF-8")
    firstrow = filehandle.readline()
    for line in filehandle:
        if line != "\n":
            Row = line.rstrip("\n")
            Columns = Row.split(";")
            Timestamp = TIMESTAMP()
            Timestamp.weekday = Columns[0]
            Timestamp.hour = Columns[1]
            Timestamp.consumption = float(Columns[2])
            Timestamp.price = float(Columns[3])
            PTimestamps.append(Timestamp)        
    filehandle.close()
    return None

WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for result in PResults:
        print(result)
    print("### Electricity consumption summary ###")
    return None

def analyseTimestamps(PTimestamps: list[TIMESTAMP], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    DayUsages: list[DAY_USAGE] = []
    for day in WEEKDAYS:
        du = DAY_USAGE()
        du.weekday = day
        DayUsages.append(du)
    for ts in PTimestamps:
        for j in range(len(WEEKDAYS)):
            if ts.weekday == DayUsages[j].weekday:
                DayUsages[j].usage += ts.consumption
                DayUsages[j].cost += ts.consumption * ts.price
    for du in DayUsages:
        PResults.append(f" - {du.weekday} usage {du.usage:.2f} kWh, cost {du.cost:.2f} €")
    DayUsages.clear()
    return None

def main() -> None:
    print("Program starting.")
    Timestamps: list[TIMESTAMP] = []
    results: list[str] = []
    filename = input("Insert filename: ")
    readFile(filename, Timestamps)
    analyseTimestamps(Timestamps, results)
    displayResults(results)
    Timestamps.clear()
    results.clear()
    print("Program ending.")
    return None

if __name__=="__main__":
    main()