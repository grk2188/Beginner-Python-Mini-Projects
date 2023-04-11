# generate secret number
"""Computer have secret number and we are
trying to guess that secret number
"""

import random
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("It's too low. Guess again!")
        elif guess > random_number:
            print("It's too high. Guess again!")
    print(f"Yay!, you have guessed the number {guess} correctly")

guess(10)