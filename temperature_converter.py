""" This program uses two functions,
celsius_to_fahrenheit() and fahrenheit_to_celsius(),
to convert temperature between Celsius and Fahrenheit.
It also uses a while loop and a menu to allow the user
to select which conversion to perform, and to exit the
program when they are done.
"""

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print("Temperature Converter")
print("=====================")

while True:
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:.2f} Celsius = {fahrenheit:.2f} Fahrenheit\n")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit:.2f} Fahrenheit = {celsius:.2f} Celsius\n")
    elif choice == 3:
        print("Exit the program...")
        break
    else:
        print("Invalid choice. Please try again.\n")





