print("Program starting.\nInsert two integers.")
num1 = int(input("Insert first integer: "))
num2 = int(input("Insert second integer: "))
print("Comparing inserted integers.")
if (num1 == num2):
    print("Integers are the same.")
elif num1 < num2:
    print("Second integer is greater.")
elif num1 > num2:
    print("First integer is greater.")
sum = num1 + num2
print(f"Adding integers together.\n{num1} + {num2} = {sum}")
print("Checking the parity of the sum...")
parity = int(sum % 2)
if parity == 0:
    print("Sum is even.")
elif parity > 0:
    print("Sum is odd.")
print("Program ending.")