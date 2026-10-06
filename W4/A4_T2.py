print("Program starting.\n")
num1 = int(input("Insert starting value: "))
num2 = int (input("Insert stopping value: "))
print("\nStarting for-loop: ")
for n in range(num1, num2+1):
    print(n, end = " ")
print("\n" *2 + "Program ending.")