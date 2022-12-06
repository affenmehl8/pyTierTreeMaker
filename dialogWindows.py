from tkinter import Tk, Canvas, LAST, simpledialog, Text, END, Label, ttk, Button
from tkinter.ttk import Entry, Combobox


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


class AddNode:
    def __init__(self):
        self.root = Tk()
        self.root.title("Add Node")
        #self.root.geometry("10x10")
        canvas = Canvas(self.root)
        canvas.grid(row=0,column=0, padx=10, pady=10)
        lbl_tier = Label(canvas, text="Tier")
        lbl_tier.grid(row=0,column=0)
        lbl_text = Label(canvas, text="Text")
        lbl_text.grid(row=0, column=1)

        selected_tier = None
        combo_tier = Combobox(canvas, textvariable=selected_tier)
        #todo get list of current tiers
        combo_tier['values'] = ("aaa", "bbbb")
        combo_tier.grid(row=1, column=0)

        selected_text = None
        input_text = ttk.Entry(self.root, textvariable=selected_text)
        input_text.grid(row=1, column=1)

        btn_ok = Button(self.root, text="Ok")
        btn_ok.grid(row=2, column=0)

        btn_cancel = Button(self.root, text="Cancel")
        btn_cancel.grid(row=2, column=1)

    def run(self):
        self.root.mainloop()

class RemoveNode:
    def __init__(self):
        self.root = Tk()
        self.root.title("Remove Node")
        # self.root.geometry("10x10")
        canvas = Canvas(self.root)
        canvas.grid(row=0, column=0, padx=10, pady=10)
        lbl_tier = Label(canvas, text="Tier")
        lbl_tier.grid(row=0, column=0)
        lbl_text = Label(canvas, text="Text")
        lbl_text.grid(row=0, column=1)

        selected_tier = None
        combo_tier = Combobox(canvas, textvariable=selected_tier)
        # todo get list of current tiers
        combo_tier['values'] = ("aaa", "bbbb")
        combo_tier.grid(row=1, column=0)

        selected_node = None
        combo_node= Combobox(canvas, textvariable=selected_node)
        # todo get list of current texts
        combo_node['values'] = ("aaa", "bbbb")
        combo_node.grid(row=1, column=1)

        btn_ok = Button(self.root, text="Ok")
        btn_ok.grid(row=2, column=0)

        btn_cancel = Button(self.root, text="Cancel")
        btn_cancel.grid(row=2, column=1)

    def run(self):
        self.root.mainloop()




test = AddNode()
test.run()
test2 = RemoveNode()
test2.run()
