# Hayden Whitney
# 3/19
# D & D Companion

import random
from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.label = Label(text="Welcome to your D & D companion!")
        self.label.grid()
        self.grid()
        self.create_widgets()
        self.exp = 0

    def create_widgets(self):
        self.button = Button(self, height="3", width="5")
        self.button["text"] = "Experience"
        self.button["command"] = self.exp
        self.button.grid()

    def exp(self):
        add = int(input("Enter the amount of experience points earned: "))
        self.exp += add
        if 0 > self.exp < 300:
            level = 1
            proficiency_bonus = 2
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 300 <= self.exp < 900:
            level = 2
            proficiency_bonus = 2
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 900 <= self.exp < 2700:
            level = 3
            proficiency_bonus = 2
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 2700 <= self.exp < 6500:
            level = 4
            proficiency_bonus = 3
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 6500 <= self.exp < 14000:
            level = 5
            proficiency_bonus = 3
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 14000 <= self.exp < 23000:
            level = 6
            proficiency_bonus = 3
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 23000 <= self.exp < 34000:
            level = 7
            proficiency_bonus = 3
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 34000 <= self.exp < 48000:
            level = 8
            proficiency_bonus = 3
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 48000 <= self.exp < 64000:
            level = 9
            proficiency_bonus = 4
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 64000 <= self.exp < 85000:
            level = 10
            proficiency_bonus = 4
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 85000 <= self.exp < 100000:
            level = 11
            proficiency_bonus = 4
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 100000 <= self.exp < 120000:
            level = 12
            proficiency_bonus = 4
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 120000 <= self.exp < 140000:
            level = 13
            proficiency_bonus = 5
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 140000 <= self.exp < 165000:
            level = 14
            proficiency_bonus = 5
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 165000 <= self.exp < 195000:
            level = 15
            proficiency_bonus = 5
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 195000 <= self.exp < 225000:
            level = 16
            proficiency_bonus = 5
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 225000 <= self.exp < 265000:
            level = 17
            proficiency_bonus = 6
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 265000 <= self.exp < 305000:
            level = 18
            proficiency_bonus = 6
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 305000 <= self.exp < 355000:
            level = 19
            proficiency_bonus = 6
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif self.exp >= 355000:
            level = 20
            proficiency_bonus = 6
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")


root = Tk()
root.title("D & D Companion")
root.geometry("300x300")
app = Application(root)
root.mainloop()
