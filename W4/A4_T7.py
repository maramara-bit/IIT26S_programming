print("Program starting.\n")
print("Check multiplicative persistence.")
num1 = (input("Insert an integer: ")) 
#Persistence steps
step = 0
while len(num1) > 1:
    step += 1
    product = 1
#Checking current number
    for n in range(len(num1)):
        number = int(num1[n])
        product = product * number
        if n == len(num1) -1:
            print(number, end="")
        else:
            print(f"{number}*", end="")
#End of for loop
    print(f" = {product}")
    num1 = str(product)
#End of while loop      
print("No more steps.")   
print(f"\nThis program took {step} step(s).\n")
print("Program ending.")