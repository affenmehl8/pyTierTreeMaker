import tkinter
import warnings
from tkinter import simpledialog, messagebox

import dialogWindows
from TreeComponents import *
from dialogWindows import *


class Arrow:
    pass#todo contains arrow itself (if possible), left node, right node

class MainWindow:
    latin_numbers = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX')
    __max_tiers = 20
    __tier_font_size = 30
    __tiers_list = [] #ICH BRAUCH HIER NEN 2D Array anderst gehts nich, um die höhen der einzelnen nodes zu bestimmen und zu addieren, damit die schwule leiste richtig funktioniert!!!!!!!!!!!!!!!!!!!!!
    __tiercount = 10

    def __init__(self, height=360, width=480, one_tier_width = 500):

        self.__height = height
        self.__one_tier_width = one_tier_width

        self.root = Tk()
        self.root.title("Tier Tree Maker")
        self.root.geometry("{0}x{1}".format(width, height))

        self.main_canvas = Canvas(self.root)
        self.__xscrollbar = Scrollbar(self.root, orient="horizontal", command=self.main_canvas.xview)
        self.__xscrollbar.pack(side=BOTTOM, fill=X)
        self.__yscrollbar = Scrollbar(self.root,orient="vertical", command=self.main_canvas.yview)
        self.__yscrollbar.pack(side=RIGHT, fill=Y)
        self.main_canvas.configure(xscrollcommand=self.__xscrollbar.set, yscrollcommand=self.__yscrollbar.set)

        self.__create_menu()

    def new_file(self):
        answer = None
        while (type(answer)!=int) or ((type(answer)==int) and answer > self.__max_tiers):
            try:
                error_message = "Please input an integer number"

                answer = simpledialog.askstring("New Tree", "How many tiers do you want? (max. {})".format(self.__max_tiers))
                answer = int(answer)
                if answer > self.__max_tiers:
                    error_message = 'maximum amount of supported tiers is {}. Go lower!'.format(self.__max_tiers)
                    raise ValueError()
                print(answer, type(answer))
            except ValueError:
                messagebox.showwarning(title="Warning", message=error_message)
            except TypeError:
                return


        #clear everything before creating new
        self.main_canvas.delete("all")
        self.__create_tiers(answer)
        #TODO falls schon was auf dem canvas existiert ne box mit z.b. all unsaved changes of the current tree will be lost (Ok, Cancel)
        # vlt ne fct contains_nodes() -> canvas children durchloopen nach nodes und dass obige

    def open_file(self):
        pass
    def save_file(self):
        pass

    def add_node(self):
        pass
    def remove_node(self):
        pass
    def add_arrow(self):
        add_remove_node = AddRemoveNode()
        add_remove_node.run()
    def remove_arrow(self):
        pass
    def add_tier(self):
        pass
    def remove_tier(self):
        pass#todo tricky weil dependences, dann alle nodes da auch löschen und alle abh. pfeile


    def __create_menu(self):
        menubar = Menu()
        self.root.config(menu=menubar)

        menu_file = Menu(menubar) #todo die funktionen der commands logischerweise

        menu_file.add_command(label="New", command=lambda: self.new_file())
        menu_file.add_command(label="Open")
        menu_file.add_command(label="Save")
        menubar.add_cascade(label="File", menu=menu_file)

        menu_edit = Menu(menubar)
        menu_edit.add_command(label="Add/Remove Node", command=lambda : self.add_remove_arrow())
        menu_edit.add_command(label="Add/Remove Arrow")
        menu_edit.add_separator()
        menu_edit.add_command(label="Add Tier")
        menu_edit.add_command(label="Remove Tier") #TODO if contains nodes, are you sure blabla dialogwindow
        menubar.add_cascade(label="Edit", menu=menu_edit)


    def __create_tiers(self, tiercount = 10):
        if tiercount > self.__max_tiers:
            warnings.warn("Max value for tiercount is {}!".format(self.__max_tiers))
        else:
            __tiercount = tiercount
        def _configure(event):
            print("EVENT FIRED!!!!!")
            max_amt_nodes = self.get_max_height()
            node_height = Node.get_height(self)
            self.main_canvas.configure(scrollregion=(0,0,self.__one_tier_width*__tiercount,self.main_canvas.winfo_height()+ max_amt_nodes*node_height)) #x1,y1,x2,y2 #todo maybe change __height to winfo_height()
        def _on_mousewheel(event):
            self.main_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        self.main_canvas.bind('<Configure>', _configure)
        self.main_canvas.bind_all("<MouseWheel>", _on_mousewheel)



        for x in range(__tiercount):
            frame = Frame(self.main_canvas, highlightbackground="black", highlightthickness=0)

            #Top enumaration Numbers
            title_text = Text(frame, height=0, font=('Times New Roman', self.__tier_font_size, 'bold'), highlightthickness=1)
            title_text.insert(END, self.latin_numbers[x])
            title_text.configure(state="disabled")
            title_text.pack(side=TOP)

            #Canvases for nodes
            tier_canvas = Canvas(frame, width=self.__one_tier_width, height=self.__height)
            tier_canvas.pack(side=TOP, anchor="nw")

            self.main_canvas.create_window(x*self.__one_tier_width, 0, window=frame, anchor='nw')

            self.__tiers_list.append(tier_canvas)
        self.main_canvas.pack(fill="both", expand=True)
        self.main_canvas.event_generate("<Configure>")

    def add_node_to_tier(self, tier_num, node_text):
        sub_canvas = self.__tiers_list[tier_num-1]
        node = Node(sub_canvas, int(self.__one_tier_width/9), node_text) #don't ask
        node.get_node().pack(side=TOP, anchor="nw", padx=10, pady=10)


    def get_max_height(self):
        sum_max_nodes = 0
        for i in range(len(self.__tiers_list)):
            nodes_per_tier = 0
            for j in self.__tiers_list[i].winfo_children():
                nodes_per_tier += 1
            if sum_max_nodes < nodes_per_tier:
                sum_max_nodes = nodes_per_tier
        return sum_max_nodes

    def run(self):
        self.root.mainloop()
        #TODO onclose: if unsaved changes, warnwindow: "do you wanna close without saving?"