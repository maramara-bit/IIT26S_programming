print("Program starting.\n")
num1 = int(input("Insert starting value: "))
num2 = int(input("Insert stopping value: "))
print("\nStarting for-loop: ")
for n in range(num1, num2+1):
    if n==num2:
        print(n, end="")
    else:
        print(n, end=" ")
print("\n\nProgram ending.")