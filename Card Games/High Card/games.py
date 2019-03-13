# Hayden Whitney
# 2/19

import random
import time
import cards


def yes_no(question):
    """Asks the given question and repeats it until an answer is given in y/n format. the response is returned."""
    response = ""
    while response != "y" and response != "n":
        response = input(question).lower()
    return response


def input_number(question, low, high):
    while True:
        num = input(question)
        try:
            num = int(num)
            if num in range(low, high + 1):
                return num
            else:
                print("Please enter a valid number within " + low + " and " + high + ".")
                input_number()
        except:
            print("That was not a number.")


def roll(dice):
    """Rolls a dice with the given number of 'sides' and returns the number rolled."""
    dice_roll = random.randint(1, dice)
    return dice_roll


def switch_turn(num_players, turn):
    if turn < num_players - 1:
        turn += 1
    else:
        turn = 0
    return turn


def winner_congrats(winner):
    print("Congratulations!")
    print("...")
    time.sleep(1)
    print(winner, "is the winner!")


class Player(object):
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name
        rep = rep + " " + str(self.score)
        return rep


if __name__ == "__main__":
    print("Your ran this module directly and did not 'import' it")
    input("\n\nPress the enter key to exit.")
