__author__ = 'QJ_H'

"""
猜数字游戏
"""
import random

guessesTaken = 0

print("Hello! What is your name?")
myName = input()

guessedNumber = random.randint(1, 20)

print("Well, %s, I am thinking of a number between 1 and 20" % myName)

while guessesTaken < 6:
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    guessesTaken += 1

    if guess == guessedNumber:
        print("Good job, %s! You guessed my number in %d guesses!" %(myName ,guessesTaken))
    elif guess > guessedNumber:
        print("Your guess is to high")
    elif guess < guessedNumber:
        print("Your guess is to low")

if guessesTaken >= 6:
    print("Nope, The number I was thinking of was %d" %guessedNumber)
