import time

username = "gopi"
password = "hridan"

username_input = input('Username: ')
password_input = input('Password: ')

if username_input == username and password_input == password:
    print("Access granted")
    print("please wait....")
    time.sleep(7)
    print("Ok... Loading...")
    time.sleep(2)
    print("....")
    print("Alright you have security clearance.")

elif username_input == username and password_input != password:
    print("Password incorrect")
elif username_input != username and password_input == password:
    print("username incorrect")
else:
    print("you must check both field correctly...")
