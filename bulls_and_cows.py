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
    if guessed_number[0] == "0":
        print("Your number cannot start with 0!")
        return
    elif "exit" in guessed_number:
        print("We are sorry you are leaving, see you next time!")
        exit()
    elif not guessed_number.isdigit():
        print("You have not entered a number!")
        return
    elif not len(guessed_number) == 4:
        print("You need to put 4-digit number!")
        return
    else:
        compare_input(guessed_number, guessing_number, attempts)


def compare_input(guessed_number, guessing_number, attempts):
    bulls = 0
    cows = 0
    if guessed_number == guessing_number:
        print(f"CG, you won! It took you {attempts} attempts!")
        exit()
    else:
        for i in range(4):
            if guessed_number[i] == guessing_number[i]:
                bulls += 1
            elif guessed_number[i] in guessing_number:
                cows += 1

    if bulls == 1 and cows == 1:
        print(f"You have {bulls} bull and {cows} cow")
    elif bulls == 1:
        print(f"You have {bulls} bull and {cows} cows")
    elif cows == 1:
        print(f"You have {bulls} bulls and {cows} cow")
    else:
        print(f"You have {bulls} bulls and {cows} cows")
    print(separator, sep="\n")
    return


def main():
    guessing_number = generate_number()
    attempts = 0
    print(guessing_number)

    while True:
        if attempts == 0:
            guessed_number = (input("Enter the number: "))
            print(separator, sep="\n")
        else:
            guessed_number = (input("Try it again: "))
            print(separator, sep="\n")

        print(f">>> " + guessed_number)
        validate_input(guessed_number, guessing_number, attempts)
        attempts += 1


if __name__ == "__main__":
    main()
