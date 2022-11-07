from tkinter import *

class Node:
    __height_const = 1
#todo minimize width with text
#todo set maxwidth
    def __init__(self, master, width, text = ""):
        self.frame = Frame(master, highlightbackground="black", highlightthickness=1)

        empty_text = Text(self.frame, height=self.__height_const, state="disabled", width=width)
        empty_text.grid(column=0, row=0)

        check = Checkbutton(self.frame)
        check.grid(column=1, row=0)

        main_text = Text(self.frame, height=3 * self.__height_const, width=width)
        main_text.insert(END, text)
        main_text.grid(column=0, row=1)

    def get_node(self):
        return self.frame


class Arrow:
    pass
