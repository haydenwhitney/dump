# Hayden Whitney
# 3/19
# Demonstrates a label

from tkinter import *

root = Tk()
root.title("Labeler")
root.geometry("500x500")

app = Frame(root)
app.grid()

lbl = Label(app, text="I'm a label!")
lbl.grid()

root.mainloop()



class Application(Frame):
    """GUI application that counts button clicks"""

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.count = 0
        self.label = Label(app, text="Count: 0")
        self.label.grid()
        self.create_widgets()

    def create_widgets(self):
        self.button = Button(self)
        self.button["text"] = " + "
        self.button["command"] = self.add()
        self.button.grid()
        self.button2 = Button(self)
        self.button2["text"] = " - "
        self.button2["command"] = self.minus()

    def add(self):
        """Increases click count by 1 and displays the new total."""
        self.count += 1
        self.label["text"] = "Count: " + str(self.count)

    def minus(self):
        """Decreases click count by 1 and displays the new total."""
        self.count -= 1
        self.label["text"] = "Count: " + str(self.count)


root = Tk()
root.title("Counter")
root.geometry("300x300")
app = Application(root)
root.mainloop()