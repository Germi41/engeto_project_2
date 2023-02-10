"""
projekt1.py: Druhý projekt do Engeto Online Python Akademie
author: David Germ
email: david.germ@kiwi.com
discord: GermiCZ#2828
"""

import random

def main():
    game_runs = True
    guesing_number = random.randint(1000, 9999)

    while game_runs:
        guessed_number = int(input("Enter the number:"))
        print(guesing_number)
        print(guessed_number)
        if guessed_number == guesing_number:
            game_runs = False

if __name__ == "__main__":
    main()
