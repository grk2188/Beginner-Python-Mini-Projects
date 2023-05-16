import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*(){}[]<>?")

def password_generate():
    password_length = int(input("How long you want to generate a password: "))

    random.shuffle(characters)
    password = []

    for _ in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)

option = input("Do you want to generate a passowrd? (Yes/No): ").lower()

if option == "yes":
    password_generate()
elif option == "no":
    print("Program ended.")