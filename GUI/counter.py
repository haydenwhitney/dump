# Hayden Whitney
# 3/19
# Counts how many times the user has clicked a button

from tkinter import *


class Application(Frame):
    """GUI application that counts button clicks"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.label = Label(text="Count: 0")
        self.label.grid()
        self.grid()
        self.button_clicks = 0
        self.create_widgets()

    def create_widgets(self):
        self.button = Button(self, height="3", width="5")
        self.button["text"] = "+"
        self.button["command"] = self.add
        self.button.grid()
        self.button2 = Button(self, height="3", width="5")
        self.button2["text"] = "-"
        self.button2["command"] = self.subtract
        self.button2.grid(row=0, column=1)

    def add(self):
        """Increases click count by 1 and displays the new total."""
        self.button_clicks += 1
        self.label["text"] = "Count: " + str(self.button_clicks)

    def subtract(self):
        """Decreases click count by 1 and displays the new total."""
        self.button_clicks -= 1
        self.label["text"] = "Count: " + str(self.button_clicks)


root = Tk()
root.title("Counter")
root.geometry("300x300")
app = Application(root)
root.mainloop()
