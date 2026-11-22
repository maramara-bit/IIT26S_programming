def displayNumbers(List):
    for i in range(len(List)):
        print(f"- Index {i} => Ordinal {i+1} => Integer {List[i]}")

def collectNumbers():
    positiveNumbers = [] 
    while True:
        number = input("Insert positive integer(negative stops): ")
        if number == "": 
            print("Error!")
            continue
        else:
            number = int(number)  
        if number < 0:
            print("Stopped collecting positive integers.")
            break
        elif number == 0:
            print("Error!")
        else:
            positiveNumbers.append(number)
    return positiveNumbers
    
def main():
    print("Program starting.")
    print("Collect positive integers.")
    numberList = collectNumbers()
    if len(numberList) > 0:
        print(f"Displaying {len(numberList)} integers:")
        displayNumbers(numberList)
    else:
        print("No integers to display.")
    print("Program ending.")


if __name__=="__main__":
    main()