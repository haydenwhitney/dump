# Hayden Whitney
# 3/19
# How to use check boxes to determine favorite movies

# from tkinter import *
#
#
# class Application(Frame):
#     def __init__(self, master):
#         super(Application, self).__init__(master)
#         self.grid()
#         self.create_widgets()
#
#     def create_widgets(self):
#         self.label = Label(self, text="Choose your favorite movie types.")
#         self.label.grid(row=1, column=0, sticky=W)
#         self.instructions = Label(self, text="Select all that apply: ")
#         self.instructions.grid(row=2, column=0, sticky=W)
#         self.likes_comedy = BooleanVar()
#         self.comedy = Checkbutton(self, text="Comedy", variable=self.likes_comedy, command=self.update_text)
#         self.comedy.grid(row=3, column=0, sticky=W)
#         self.likes_drama = BooleanVar()
#         self.drama = Checkbutton(self, text="Drama", variable=self.likes_drama, command=self.update_text)
#         self.drama.grid(row=4, column=0, sticky=W)
#         self.likes_romance = BooleanVar()
#         self.romance = Checkbutton(self, text="Romance", variable=self.likes_romance, command=self.update_text)
#         self.romance.grid(row=5, column=0, sticky=W)
#         self.results = Text(self, width=40, height=5, wrap=WORD)
#         self.results.grid(row=6, column=0, sticky=W)
#
#     def update_text(self):
#         likes = ""
#         if self.likes_comedy.get():
#             likes += "You like comedic movies.\n"
#         if self.likes_drama.get():
#             likes += "You like dramatic movies.\n"
#         if self.likes_romance.get():
#             likes += "You like romantic movies.\n"
#         self.results.delete(0.0, END)
#         self.results.insert(0.0, likes)
#
#
# root = Tk()
# root.title("Survey")
#
# app = Application(root)
#
# root.mainloop()

from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self, text="Choose your favorite movie types.")
        self.label.grid(row=1, column=0, sticky=W)
        self.instructions = Label(self, text="Select all that apply: ")
        self.instructions.grid(row=2, column=0, sticky=W)
        self.favorite = StringVar()
        self.favorite.set(None)
        Radiobutton(self,
                    text="Comedy",
                    variable=self.favorite,
                    value="comedic.",
                    command=self.update_text
                    ).grid(row=3, column=0, sticky=W)
        Radiobutton(self,
                    text="Drama",
                    variable=self.favorite,
                    value="dramatic.",
                    command=self.update_text
                    ).grid(row=4, column=0, sticky=W)
        Radiobutton(self,
                    text="Romance",
                    variable=self.favorite,
                    value="romantic.",
                    command=self.update_text
                    ).grid(row=5, column=0, sticky=W)
        self.results = Text(self, width=40, height=5, wrap=WORD)
        self.results.grid(row=6, column=0, sticky=W)

    def update_text(self):
        message = "Your favorite types of movie are "
        message += self.favorite.get()
        self.results.delete(0.0, END)
        self.results.insert(0.0, message)


root = Tk()
root.title("Survey")

app = Application(root)

root.mainloop()
