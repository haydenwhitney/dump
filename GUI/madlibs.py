# Hayden Whitney
# 3/19
# A simple madlib generator

from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.title = Label(self, text="placeholder")
        self.title.grid(row=1, columnspan=2, sticky=W)

        self.label_1 = Label(self, text="placeholder")
        self.label_1.grid(row=2, column=1, sticky=W)
        self.entry_1 = Entry(self)
        self.entry_1.grid(row=2, column=2, sticky=W)

        self.label_2 = Label(self, text="placeholder")
        self.label_2.grid(row=3, column=1, sticky=W)
        self.entry_2 = Entry(self)
        self.entry_2.grid(row=3, column=2, sticky=W)

        self.label_3 = Label(self, text="placeholder")
        self.label_3.grid(row=4, column=1, sticky=W)
        self.entry_3 = Entry(self)
        self.entry_3.grid(row=4, column=2, sticky=W)

        self.label_4 = Label(self, text="placeholder")
        self.label_4.grid(row=5, column=1, sticky=W)
        self.checkbutton_1 = Checkbutton(self, text="placeholder")
        self.checkbutton_1.grid(row=5, column=2, sticky=W)
        self.checkbutton_2 = Checkbutton(self, text="placeholder")
        self.checkbutton_2.grid(row=5, column=3, sticky=W)
        self.checkbutton_3 = Checkbutton(self, text="placeholder")
        self.checkbutton_3.grid(row=5, column=4, sticky=W)

        self.label_5 = Label(self, text="placeholder")
        self.label_5.grid(row=6, column=1, sticky=W)
        self.choice = StringVar()
        self.choice.set(None)
        self.radiobutton_1 = Radiobutton(self, text="placeholder", variable=self.choice, value="1")
        self.radiobutton_1.grid(row=6, column=2, sticky=W)
        self.radiobutton_2 = Radiobutton(self, text="placeholder", variable=self.choice, value="2")
        self.radiobutton_2.grid(row=6, column=3, sticky=W)
        self.radiobutton_3 = Radiobutton(self, text="placeholder", variable=self.choice, value="3")
        self.radiobutton_3.grid(row=6, column=4, sticky=W)

        self.button = Button(self, text="placeholder")
        self.button.grid(row=7, column=1, sticky=W)

        self.textbox = Text(self, height=6, wrap=WORD)
        self.textbox.grid(row=8, column=1, columnspan=4, sticky=W)


root = Tk()
root.title("Madlib Generator")

app = Application(root)

root.mainloop()
