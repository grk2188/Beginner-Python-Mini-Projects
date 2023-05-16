import random

def dice_roll():

     roll = input("Roll a dice? (Yes/No): ")

     while roll == "yes":
         dice1 = random.randint(1,6)
         dice2 = random.randint(1,6)

         print(f"dice rolled {dice1} and {dice2}")

         roll = input("Roll Again? (Yes/No): ")

dice_roll()