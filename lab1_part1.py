# Lab 1, Part 1.
# To refresh your memory of Python, write a 'guess the number' game.
# The computer should 'think' of a random number within a certain range, and challenge the user to guess the number.
# Provide feedback and hints for the user; such as "too high" or "too low".

import random


def generate_number(u_limit):

    return random.randrange(u_limit)


def get_input(range_max):
        try:
            # get a number from user, try to cast to int
            guess = int(input("Please enter a number between 0 and " + str(range_max) + ":\n"))
            # if casting is successful, exit loop and return guess
            if 0 < guess < range_max:
                return guess
            else:
                return False
        except ValueError:
            # if the guess is not a number print error message and try again
            print("Was that a number?")


if __name__ == '__main__':

    # change r_max to set upper limit of range
    range_max = 10
    target = None
    guess = None
    guess_count = 0

    target = generate_number(range_max)

    while True:
        guess = get_input(range_max)
        if guess is int:
            break

    while guess != target:
        guess_count += 1
        if guess > target:
            print("Too high")
        else:
            print("Too low")
        guess = get_input()

    print("You guessed correct. The number was " + str(target))
