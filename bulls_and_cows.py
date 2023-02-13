"""
projekt1.py: Druhý projekt do Engeto Online Python Akademie
author: David Germ
email: david.germ@kiwi.com
discord: GermiCZ#2828
"""

import random

def main():
    game_runs = True
    guessing_number = str(random.randint(1000, 9999))
    attempts = 0

    while game_runs:
        guessed_number = (input("Enter the number:"))
        attempts += 1
        bulls = 0
        cows = 0
        print(guessing_number)
        print(guessed_number)

        if guessed_number == guessing_number:
            print(f"CG, you won! It took you {attempts} attempts!")
            game_runs = False

        elif "exit" in guessed_number:
            print("We are sorry your are leaving, see you next time!")
            game_runs = False

        else:
            for i in range(4):
                if guessed_number[i] == guessing_number[i]:
                    bulls += 1
                elif guessed_number[i] in guessing_number:
                    cows += 1
        print(f"You have {bulls} bulls and {cows} cows")

if __name__ == "__main__":
    main()
