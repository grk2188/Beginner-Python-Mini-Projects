# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

print('Welcome to my computer quiz!')
play = input("Do you want to play? ")

if play.lower() != "yes":
    quit()
score = 0

print("Okay!, Let's play")
answer = input("What is RAM stands for: ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is CPU stand for: ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What is OS stand for: ")
if answer.lower() == "operating system":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
answer = input("Wnat is HDD stand for: ")
if answer.lower() == "hard disk drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got", score, "scores")
print("You got",(score/4)*100,"%.")
