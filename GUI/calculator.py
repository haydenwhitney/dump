# Hayden Whitney
# 3/19
# A simple calculator

from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.textbox = Text(self, height=3, width=22, wrap=WORD)
        self.textbox.grid(row=1, column=1, columnspan=4, sticky=W)
        self.seven = Button(self, text="7", width=5, height=2)
        self.seven.grid(row=2, column=1, sticky=W)
        self.eight = Button(self, text="8", width=5, height=2)
        self.eight.grid(row=2, column=2, sticky=W)
        self.nine = Button(self, text="9", width=5, height=2)
        self.nine.grid(row=2, column=3, sticky=W)
        self.divide = Button(self, text="/", width=5, height=2)
        self.divide.grid(row=2, column=4, sticky=W)
        self.four = Button(self, text="4", width=5, height=2)
        self.four.grid(row=3, column=1, sticky=W)
        self.five = Button(self, text="5", width=5, height=2)
        self.five.grid(row=3, column=2, sticky=W)
        self.six = Button(self, text="6", width=5, height=2)
        self.six.grid(row=3, column=3, sticky=W)
        self.multiply = Button(self, text="X", width=5, height=2)
        self.multiply.grid(row=3, column=4, sticky=W)
        self.one = Button(self, text="1", width=5, height=2)
        self.one.grid(row=4, column=1, sticky=W)
        self.two = Button(self, text="2", width=5, height=2)
        self.two.grid(row=4, column=2, sticky=W)
        self.three = Button(self, text="3", width=5, height=2)
        self.three.grid(row=4, column=3, sticky=W)
        self.subtract = Button(self, text="-", width=5, height=2)
        self.subtract.grid(row=4, column=4, sticky=W)
        self.zero = Button(self, text="0", width=5, height=2)
        self.zero.grid(row=5, column=1, sticky=W)
        self.clear = Button(self, text="C", width=5, height=2)
        self.clear.grid(row=5, column=2, sticky=W)
        self.solve = Button(self, text="=", width=5, height=2)
        self.solve.grid(row=5, column=3, sticky=W)
        self.add = Button(self, text="+", width=5, height=2)
        self.add.grid(row=5, column=4, sticky=W)

    def one(self):
        

root = Tk()
root.title("Calculator")

app = Application(root)

root.mainloop()
