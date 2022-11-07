import logging
import time
import warnings
from tkinter import *
from tkinter import ttk

from TreeComponents import *

class MainWindow:
    latin_numbers = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX')

    def __init__(self, y=0, x=0):

        self.height = y
        self.width = x
        resolution=""
        if self.height==0 or self.width==0:
            self.height = 360
            self.width = 480
        resolution="{}x{}".format(self.width,self.height)
        self.root = Tk()
        self.root.geometry(resolution)

        self.__create_menu()
        self.__create_tiers()

    def __create_menu(self):
        menubar = Menu()
        self.root.config(menu=menubar)

        menu_file = Menu(menubar) #todo die funktionen der commands logischerweise
        menu_file.add_command(label="New")
        menu_file.add_command(label="Open")
        menu_file.add_command(label="Save")
        menubar.add_cascade(label="File", menu=menu_file)

        menu_add = Menu(menubar)
        menu_add.add_command(label="Add Node")
        menu_add.add_command(label="Add Arrow")
        menu_add.add_command(label="Add Tier")
        menu_add.add_command(label="Insert Tier")
        menubar.add_cascade(label="Add", menu=menu_add)


    def __create_tiers(self, tiercount = 10):

        if tiercount > 20:
            warnings.warn("Max value for tiercount is 20!")
            tiercount = 10
        canvas = Canvas(self.root)


        def _configure(event):
            # print(canvas.winfo_width(), canvas.winfo_height())
            canvas.configure(scrollregion=(0,0,9999,9999)) #x,y,x,y

        canvas.bind('<Configure>', _configure)

        xscrollbar = Scrollbar(self.root, orient="horizontal", command=canvas.xview)
        xscrollbar.pack(side=BOTTOM, fill=X)
        yscrollbar = Scrollbar(self.root,orient="vertical", command=canvas.yview)
        yscrollbar.pack(side=RIGHT, fill=Y)
        canvas.pack(fill="both", expand=True)
        canvas.configure(xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)


        for x in range(tiercount): #todo try to remove hardcoded sizes, fixed sized for frames and it'S contents!
            frame = Frame(canvas, highlightbackground="black", highlightthickness=1)
            title_text = Text(frame, height=1, font=('Times New Roman', 30, 'bold'), highlightthickness=1)
            title_text.insert(END, self.latin_numbers[x])
            title_text.configure(state="disabled")
            title_text.pack(side=TOP)

            field_text = Text(frame)
            field_text.insert(END, "blalbablalbalbalbalb")
            field_text.pack(side=TOP)

            # frame.pack(side=LEFT)
            canvas.create_window(x*500, 0, window=frame, anchor='nw')




    def run(self):
        self.root.mainloop()
        #TODO onclose: if unsaved changes, warnwindow: "do you wanna close without saving?"