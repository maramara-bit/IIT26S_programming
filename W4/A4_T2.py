print("Program starting.")
num1 = int(input("Insert starting value: "))
num2 = int (input("Insert stopping value: "))
print("Starting for-loop:")
for n in list(range(num1, num2+1)):
    print(n)
print("Program ending.")
#replace the print-command end character with space
#so that all the iterations can be printed on the s
# ame row. Last iteration might require additional 
# logic to get rid of the extra space at the end.
