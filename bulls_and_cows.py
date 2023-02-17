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
def main():
    guessing_number = generate_number()
    attempts = 0

    while True:
        guessed_number = (input("Enter the number:"))
        attempts += 1
        bulls = 0
        cows = 0
        print(guessing_number)
        print(guessed_number)

        if guessed_number == guessing_number:
            print(f"CG, you won! It took you {attempts} attempts!")
            break

        elif "exit" in guessed_number:
            print("We are sorry your are leaving, see you next time!")
            break

        else:
            for i in range(4):
                if guessed_number[i] == guessing_number[i]:
                    bulls += 1
                elif guessed_number[i] in guessing_number:
                    cows += 1
        print(f"You have {bulls} bulls and {cows} cows")

if __name__ == "__main__":
    main()
