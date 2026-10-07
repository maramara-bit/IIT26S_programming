print("Program starting.")
num1 = int(input("Insert a positive integer: "))
#If odd, multiply by three, add one, if even divide by two
step = 0
while True:
    print(num1, end="")
    if num1 == 1:
        break
    print(end=" -> ")
    if num1 % 2 != 0:
        num1 = num1*3+1
        step +=1
    elif num1 % 2 == 0:
        num1 = num1//2
        step +=1
print(f"\nSequence had {step} total steps.\n")
print("Program ending.")    