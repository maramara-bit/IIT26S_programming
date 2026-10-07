print("Program starting.\n")
#Check rules
while True:
    num1 = int(input("Insert starting point: "))
    num2 = int(input("Insert stopping point: "))
    if num2 < num1:
        print("Starting point value must be less than the stopping point value.")
        break
    num3 = int(input("Insert inspection point: "))
    if num3 < num1 or num3 > num2: 
        print("Inspection value must be within the range of start and stop.")
        break
    else:#Break, cut from inspection point
        print("\nFirst loop - inspection with break:")
        for n in range(num1, num2):
            if n == num3:
                break
            print(n, end="")
        #Continue, skip inspection point
        print("\nSecond loop - inspection with continue:")
        for n in range(num1, num2):
            if n == num3:
                continue
            print(n, end="")
        break #end while loop
print("\nProgram ending.")