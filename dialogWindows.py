from tkinter import Tk, Canvas, LAST, simpledialog, Text, END
from tkinter.ttk import Entry

#todo onclose save unchanged
#todo die interaktionen für menubars
# from tkinter import simpledialog
# from mainWindow import MainWindow
#
#
# class DialogWindow:
#     def __init__(self, main_window):
#         self.master = main_window
#     def new_file(self):
#         answer = simpledialog.askstring("New Tree", "How many tiers do you want? (max. 20)")
#         self.master.__create_tiers()


class AddRemoveNode:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root)
        self.canvas.configure(highlightthickness=5, highlightbackground="green")
        self.canvas.pack(expand=True, fill="both")
        self.tmpfct()

    def tmpfct(self):
        height = 5
        width = 5

        b = Text(self.canvas, height=5, width=10)
        b.insert(END, "Tiers\n\n\nNodes")
        b.grid(row=0, column=0)
        b.configure(state="disabled")
        for i in range(height):  # Rows
            for j in range(1, width):  # Columns
                b = Text(self.canvas, height=5, width=10)
                b.insert(END, "sssesesss")
                b.grid(row=i, column=j)
                b.configure(state="disabled")

    def run(self):
        self.root.mainloop()
