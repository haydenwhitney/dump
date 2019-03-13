# Hayden Whitney
# 3/19
# Button Classes

from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Creates 3 useless buttons."""
        label = Label(self, text="These are buttons:", bg="#E6E6FA", fg="black")
        label.grid()

        self.b1 = Button(self, text="Button 1", fg="#273746")
        self.b1.grid()

        self.b2 = Button(self)
        self.b2.grid()
        self.b2.configure(text="Button 2")

        self.b3 = Button(self)
        self.b3.grid()
        self.b3.configure(text="Button 3")


root = Tk()
root.title("Lazy Buttons")
root.geometry("300x300")
app = Application(root)
root.mainloop()
