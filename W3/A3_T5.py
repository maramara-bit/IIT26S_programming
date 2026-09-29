print("Program starting.\n")
print("Options:\n1 - Celsius to Fahrenheit\n2 - Fahrenheit to Celsius\n0 - Exit")
choice = int(input("Your choice: "))
if choice == 1:
    celsius = int(input("Insert the amount of Celsius: "))
    print(f"{celsius}°C equals to {round(celsius*1.8+32, 1)}°F")
elif choice == 2:
    fahrenheit = int(input("Insert the amount of Fahrenheit: "))
    print(f"{fahrenheit}°F equals to {round((fahrenheit-32)/1.8, 1)}°C")
elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")