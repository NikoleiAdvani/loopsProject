# Nikolei Advani, 10/17/2016
# This program is a simple game in which the computer generates a number and the user guesses that number

import random


def playGame():
    """This asks the user if they want to play"""
    while True:
        answer = input("Would you like to play a game?")
        if answer == "yes":
            return True
        elif answer == "no":
            return False


def randomNumber():
    """This generates a random number between 1-100"""
    random_number = random.randint(1, 100)
    return random_number


def gameTime(random_number):
    """This executes the game"""
    guesses = 0
    while True:
        guess = int(input("What is my number?"))
        if guess <= 100 and guess >= 0:
            guesses += 1
            if guess == random_number:
                print("Congratulations! That is correct!")
                print("It took you", guesses, "guesses!")
                break
            elif guess > random_number:
                print("Too high!")
            else:
                print("Too low!")


def main():
    """This calls the other functions"""
    while playGame():
        gameTime(randomNumber())

main()
