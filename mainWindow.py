import warnings
from TreeComponents import *

class MainWindow:
    latin_numbers = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX')
    __tier_font_size = 30
    __tiers_list = [] #ICH BRAUCH HIER NEN 2D Array anderst gehts nich, um die höhen der einzelnen nodes zu bestimmen und zu addieren, damit die schwule leiste richtig funktioniert!!!!!!!!!!!!!!!!!!!!!

    def __init__(self, height=360, width=480, one_tier_width = 500):

        self.__height = height
        self.__one_tier_width = one_tier_width

        self.root = Tk()
        self.root.geometry("{0}x{1}".format(width, height))

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

        menu_edit = Menu(menubar)
        menu_edit.add_command(label="Add Node")
        menu_edit.add_command(label="Add Arrow")
        menu_edit.add_command(label="Add Tier")
        menu_edit.add_command(label="Insert Tier")
        menu_edit.add_separator()
        menu_edit.add_command(label="Remove Node")
        menu_edit.add_command(label="Remove Arrow")
        menu_edit.add_command(label="Remove Tier") #TODO if contains nodes, are you sure blabla dialogwindow
        menubar.add_cascade(label="Edit", menu=menu_edit)


    def __create_tiers(self, tiercount = 10):
        if tiercount > 20:
            warnings.warn("Max value for tiercount is 20!")
            tiercount = 10
        canvas = Canvas(self.root)

        def _configure(event):
            max_amt_nodes = self.get_max_height()
            node_height = Node.get_height(self)
            canvas.configure(scrollregion=(0,0,self.__one_tier_width*tiercount,canvas.winfo_height()+ max_amt_nodes*node_height)) #x1,y1,x2,y2 #todo maybe change __height to winfo_height()
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind('<Configure>', _configure)
        canvas.bind_all("<MouseWheel>", _on_mousewheel)



        xscrollbar = Scrollbar(self.root, orient="horizontal", command=canvas.xview)
        xscrollbar.pack(side=BOTTOM, fill=X)
        yscrollbar = Scrollbar(self.root,orient="vertical", command=canvas.yview)
        yscrollbar.pack(side=RIGHT, fill=Y)
        canvas.pack(fill="both", expand=True)
        canvas.configure(xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)

        for x in range(tiercount):
            frame = Frame(canvas, highlightbackground="black", highlightthickness=0)

            #Top enumaration Numbers
            title_text = Text(frame, height=0, font=('Times New Roman', self.__tier_font_size, 'bold'), highlightthickness=1)
            title_text.insert(END, self.latin_numbers[x])
            title_text.configure(state="disabled")
            title_text.pack(side=TOP)

            #Canvases for nodes
            tier_canvas = Canvas(frame, width=self.__one_tier_width, height=self.__height)
            tier_canvas.pack(side=TOP, anchor="nw")

            canvas.create_window(x*self.__one_tier_width, 0, window=frame, anchor='nw')

            self.__tiers_list.append(tier_canvas)

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