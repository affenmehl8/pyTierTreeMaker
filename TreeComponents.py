from tkinter import *

class Node:
    height_const = 1

    def __init__(self, text = "" ):
        self.frame = Frame(highlightbackground="black", highlightthickness=1)



        empty_text = Text(self.frame, height=self.height_const, state="disabled")
        empty_text.grid(column=0, row=0)

        check = Checkbutton(self.frame)
        check.grid(column=1, row=0)

        main_text = Text(self.frame, height=3 * self.height_const)
        main_text.insert(END, "bla bla bla bla")
        main_text.grid(column=0, row=1)

    def get_node(self):
        return self.frame


class Arrow:
    pass
