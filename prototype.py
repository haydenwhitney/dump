# Hayden Whitney
# 1/19
# Tamagotchi Prototype

import random


class Critter(object):
    def __init__(self, name):
        self.name = name
        self.__hunger = random.randint(0, 11)
        self.__boredom = random.randint(0, 11)

    def __pass_time(self):
        self.__hunger += 1
        self.__boredom += 1

    def play(self, name):
        print("You play with " + name + ".")
        fun = random.randint(0, 11)
        self.__boredom -= fun
        if self.__boredom < 0:
            self.__boredom = 0
        self.__pass_time()

    def talk(self, name):
        print(name + " seems to be " + self.mood + ".")
        self.__pass_time()

    def eat(self, name):
        print("You feed " + name + ".")
        food = random.randint(0, 26)
        self.__boredom -= food
        if self.__hunger < 0:
            self.__hunger = 0
        self.__pass_time()

    @property
    def mood(self):
        unhappiness = self.__hunger + self.__boredom
        if unhappiness < 10:
            mood = "happy"
        elif 10 < unhappiness < 15:
            mood = "doing okay"
        elif 15 < unhappiness < 20:
            mood = "frustrated"
        else:
            mood = "angry"
        return mood


def main():
    print("A new critter has been born!")
    name = input("Enter a name for the new critter: ").title()
    if name == "":
        print("A critter's name can't be an empty string.")
        main()
    else:
        print("Naming successful.")
    critter = Critter(name)
    choice = None
    while choice != "3":
        print("""[0] LISTEN
[1] FEED
[2] PLAY
[3] QUIT""")
        choice = input("Enter the [#] of your choice: ")
        print()
        if choice == "0":
            critter.talk(name)
        elif choice == "1":
            critter.eat(name)
        elif choice == "2":
            critter.play(name)
        elif choice == "3":
            print("Goodbye.\n")
        else:
            print("Please enter a valid choice.")
            break


main()
input("\nPress the enter key to exit.")
