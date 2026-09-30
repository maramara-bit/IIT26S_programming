print("Program starting.")
print("Testing decision structures.")
#User chooses an integer
num1 = int(input("Insert an integer: "))
#Display options
print("Options:\n1 - In one multi-branched decision\n2 - In multiple independent if-statements\n0 - Exit")
#User inputs option
choice0 = int(input("Your choice: "))
#Option 1
if choice0 == 1:
    print("Using one multi-branched decision structure.")
    if num1>=100:
        print(f"Result is {num1+11}")
    elif num1>=200:
        print(f"Result is {num1+22}")   
    elif num1>=400:
        print(f"Result is {num1+44}")  
#Option 2
elif choice0 == 2:
    print("Using multiple independent if-statements structure.")
    if num1 >= 400:
        print(f"Result is {num1+44}")
    if num1 >= 200 and num1 < 400:       
        print(f"Result is {num1+22}")
    if num1 >= 100 and num1 < 200:
        print(f"Result is {num1+11}")
#Option 3 Exit
elif choice0 == 3:
    print("Exiting...")
else:
    print("Unknown option.")                