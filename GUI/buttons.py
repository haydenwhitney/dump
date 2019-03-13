# Hayden Whitney
# 3/19
# Buttons!

from tkinter import *

root = Tk()
root.title("Labeler")
root.geometry("750x750")
root.configure(bg="#E6E6FA")

mainframe = Frame(root)
mainframe.grid()
mainframe.configure(bg="lightgray")

label = Label(mainframe, text="These are buttons:", bg="#E6E6FA", fg="black")
label.grid()

button = Button(mainframe, text="Button 1", fg="#273746")
button.grid()

button2 = Button(mainframe)
button2.grid()
button2.configure(text="Button 2")

button3 = Button(mainframe)
button3.grid()
button3["text"] = "Button 3"

root.mainloop()
