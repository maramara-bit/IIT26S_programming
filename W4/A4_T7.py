print("Program starting.\n")
print("Check multiplicative persistence.")
#Number to be multiplied
num1 = (input("Insert an integer: ")) 
#Persistence steps
step = 0
while len(num1) > 1:
    step += 1 #Keeping track of steps
    product = 1 #Tulo, multiplying with 1 does not change value
    #len(num1) returns the number of characters given in num1
    #Checking current number
    for n in range(len(num1)):#n is a specific number in range 0 to how many characters
        number = int(num1[n]) #Convert from text to integer
        product = product * number
        if n == len(num1) -1: #If range is the same as the amount of characters in num1 -1
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