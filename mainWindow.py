from tkinter import *
from TreeComponents import *

class MainWindow:
    latin_numbers = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X')

    def __init__(self, resolution = "480x360"):
        self.root = Tk()
        self.root.geometry(resolution)

        self.__create_menu()
        self.__create_tiers()

        #todo das mainframe als canvas??

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


    def __create_tiers(self, tiercount = 5):
        canvas = Canvas(self.root, width=300, height=300, scrollregion=(0,0,500,500))
        canvas.pack()

        scrollbar_horizontal = Scrollbar(canvas, orient="horizontal", command=canvas.xview) #todo doesnt work!
        scrollbar_horizontal.pack(side=BOTTOM, fill= X)
        scrollbar_vertical = Scrollbar(canvas, orient="vertical", command=canvas.yview)
        scrollbar_vertical.pack(side=RIGHT, fill=Y)
        canvas.configure(xscrollcommand=scrollbar_horizontal.set, yscrollcommand= scrollbar_vertical.set)


        for x in range(tiercount):
            frame = Frame(canvas, highlightbackground="black", highlightthickness=1)
            title_text = Text(frame, width=50, font=('Times New Roman', 30, 'bold'))
            title_text.insert(END, self.latin_numbers[x])
            title_text.pack(side=TOP)

            field_text = Text(frame)
            field_text.insert(END, "blalbablalbalbalbalb")
            field_text.pack(side=TOP)

            frame.pack(side=LEFT)




    def run(self):
        self.root.mainloop()
        #TODO onclose: if unsaved changes, warnwindow: "do you wanna close without saving?"