print("Program starting.\n")
num1 = int(input("Insert starting value: "))
num2 = int(input("Insert stopping value: "))
print("\nStarting while-loop:")
while True:
    if num1 < num2:
       print (num1, end=" ")
       num1 += 1
    elif num1 > num2:
       print(num1, end=" ")
       num1 -= 1   
    elif num1 == num2:
       print(num2)
       break
print("\nProgram ending.")

