#3
import random

number, guess = random.randint(1, 10), 0
while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))

print("Correct!")