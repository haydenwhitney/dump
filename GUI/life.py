# Hayden Whitney
# 3/19
# How to use text entry, widgets, and the grid manager

from tkinter import *


class Application(Frame):
    """GUI application that reveals the secret to longevity."""
    def __init__(self, master):
        """Initializes the frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Creates, buttons, text, and entry widgets."""
        self.label = Label(self, text="To view the secret: enter the password and click submit.")
        self.label.grid(row=1, column=0, columnspan=2)
        self.p_label = Label(self, text="Password: ")
        self.p_label.grid(row=2, column=0, columnspan=10, sticky=W)
        self.p_entry = Entry(self, show="*")
        self.p_entry.grid(row=2, column=0, sticky=E)
        self.submit = Button(self, text="Submit", command=self.reveal)
        self.submit.grid(row=3, column=0, sticky=E)
        self.secret = Text(self, width=35, height=5, wrap=WORD)
        self.secret.grid(row=4, column=0, sticky=W)

    def reveal(self):
        password = self.p_entry.get()
        if password == "jacob sucks":
            message = "Here's the secret of life......42."
        else:
            message = "That's not the correct password. I can't share the secret with you."
        self.secret.delete(0.0, END)
        self.secret.insert(0.0, message)


root = Tk()
root.title("The Secret of Life")
root.geometry("300x175")

app = Application(root)

root.mainloop()
