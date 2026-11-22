class TIMESTAMP:
    weekday: str = ""
    hour: str = ""
    consumption: float = 0.0
    price: float = 0.0

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

def displayTimestamps(PTimeStamps: list[TIMESTAMP]) -> None:
    print("Electricity usage:")
    for ts in PTimeStamps:
        total = ts.consumption * ts.price
        print(f" - {ts.weekday} {ts.hour}, price {ts.price:.2f}, consumption {ts.consumption:.2f} kWh, total {total:.2f} €")
    return None

def main() -> None:
    print("Program starting.")
    Timestamps: list[TIMESTAMP] = []
    filename = input("Insert filename: ")
    readFile(filename, Timestamps)
    displayTimestamps(Timestamps)
    Timestamps.clear()
    print("Program ending.")
    return None

if __name__=="__main__":
    main()