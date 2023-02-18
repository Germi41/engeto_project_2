"""
projekt1.py: Druhý projekt do Engeto Online Python Akademie
author: David Germ
email: david.germ@kiwi.com
discord: GermiCZ#2828
"""

import random

separator = (40 * '-')


def generate_number():
    numbers = list(range(0, 10))
    random.shuffle(numbers)

    number = numbers[:4]
    while True:
        if number[0] == 0:
            random.shuffle(number)
        else:
            number = ''.join(map(str, number))
            return number


def validate_input(guessed_number, guessing_number, attempts):
    bulls = 0
    cows = 0
    if guessed_number == guessing_number:
        print(f"CG, you won! It took you {attempts} attempts!")
        exit()

    elif "exit" in guessed_number:
        print("We are sorry you are leaving, see you next time!")
        exit()

    else:
        for i in range(4):
            if guessed_number[i] == guessing_number[i]:
                bulls += 1
            elif guessed_number[i] in guessing_number:
                cows += 1

    print(f"You have {bulls} bulls and {cows} cows")
    return True


def main():
    guessing_number = generate_number()
    attempts = 0
    print(guessing_number)

    while True:
        if attempts == 0:
            guessed_number = (input("Enter the number: "))
        else:
            guessed_number = (input("Try it again: "))

        print(f">>> " + guessed_number)
        validate_input(guessed_number, guessing_number, attempts)
        attempts += 1


if __name__ == "__main__":
    main()
