# Rock-paper-scissor game need 2 player
# rock beats scissor, scissor beats paper, paper beats rock.

import random

def play():
    print("Select your choice: ")
    user = input("'r' for rock, 's' for scissor, 'p' for paper: ").lower()
    computer = random.choice(['r', 's', 'p'])

    print("Computer choice: ", computer)

    if user == computer:
        return 'It\'s a tie'
    if is_win(user, computer):
        return 'You Won!'
    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins
    # r --> s, s --> p, p --> r
    if (player == 'r' and opponent == 's') or (player == 's'\
        and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())