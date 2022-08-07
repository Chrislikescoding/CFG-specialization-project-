import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import csv
import os
from os.path import exists, join

class MileageApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # create object, title and window size
        self.geometry('1000x800')
       # self.resizable(0, 0)
        self.title('Py-miles Expense tracker')
        self.frame = tk.Frame(self.master)
        self.frame2 = tk.Frame(self.master)

      #  self.button1 = tk.Button(self.frame2, text = 'New Window', width = 25, command = self.new_window)
       # self.button1.pack()
        self.del_rcd = tk.Button(self.frame2, text='Delete lines', command=self.del_rcd)
        self.del_rcd.pack()
        self.button2= tk.Button(self.frame2, text='save and submit',
                width=65,bg='#FF66FF', fg='white', command=self.save_csv)
        self.button2.pack()
   #     self.email_name = ttk.Entry(self.frame2, width=65,text='email address must be entered to save and submit')
     #   self.email_name.pack()


        self.label= ttk.Label(self.frame, text ="Monthly Mileage Data" )
        self.label.pack()
        self.email_address =ttk.Entry(self.frame, font=f)

        # item_amt = Entry(f1, font=f, textvariable=amtvar)
        # transaction_date = Entry(f1, font=f, textvariable=dopvar)
        self.treeview=self.create_treeview_widget()
        self.treeview.pack()
        #   self.set_buttons()
        self.frame.pack()
        # #7 Entry Widgets
        # item_name = Entry(f1, font=f)
        # item_amt = Entry(f1, font=f, textvariable=amtvar)
        # transaction_date = Entry(f1, font=f, textvariable=dopvar)
        self.frame2.pack()





       # self.treeview.grid.pack(row=0, column=0)
       # scrollbar.grid(row=0, column=1, sticky=tk.N + tk.S)
       # self.rowconfigure(0, weight=1)
       # self.columnconfigure(0, weight=1)

       # self.frame.pack()
    def set_buttons(self):
        submit_btn = tk.Button(
            self.frame2,
            text='Save Record',
            font=f,
            command=self.print_selection(event="dbl-click"),
            bg='#42602D',
            fg='white'
        )

        clr_btn = tk.Button(
            self.frame2,
            text='Clear Entry',
            font=f,
            command=None,
            bg='#D9B036',
            fg='white'
        )

        quit_btn = tk.Button(
            self.frame2,
            text='Exit',
            font=f,
            command=None,
            bg='#D33532',
            fg='white'
        )

        total_bal = tk.Button(
            self.frame2,
            text='Total Balance',
            font=f,
            command=None
        )

        total_bal = tk.Button(
            self.frame2,
            text='Total Balance',
            font=f,
            bg='#486966',
            fg='white',
            command=None
        )

        total_spent = tk.Button(
            self.frame2,
            text='Total Spent',
            font=f,
            fg='white',
            command=None
        )

        update_btn = tk.Button(
            self.frame2,
            text='Update',
            bg='#C2BB00',
            command=None,
            fg='white',
            font=f
        )

        # del_btn = tk.Button(
        #     self.frame2,
        #     text='Delete',
        #     bg='#BD2A2E',
        #     fg='white',
        #     command=None,
        #     font=f
        # )

        # 10 Button grid placement
        submit_btn.pack()
        clr_btn.pack()
        quit_btn.pack()

    def del_rcd(self):
        x= self.treeview.selection()
        for record in x:
            self.treeview.delete(record)

    def save_csv(self):
        self.label = ttk.Label(self.frame, text ="Your email address must be entered to save and submit" )
        self.label.pack()
        self.email_name = ttk.Entry(self.frame2, width=65, text='',)
        self.email_name.pack()

        with open("new.csv", "w", newline='') as myfile:
            csvwriter = csv.writer(myfile, delimiter=',')
            for row_id in self.treeview.get_children():
                row = self.treeview.item(row_id)['values']
                print('save row:', row)
                csvwriter.writerow(row)

    def get_data(self):
        path = os.getcwd()
        path: str = join(path, 'first.csv')
        print("here" + path)
        File = open(str(path))
        Reader = csv.reader(File)
        Data = list(Reader)
        return Data

    # def delete():
    #     # Get selected item to Delete
    #     selected_item = self.treeview.selection()[0]
    #     treeview.delete(selected_item)

    # def OnDoubleClick(self, event):
    #     item = self.tree.selection()[1]
    #     print("you clicked on", self.tree.item(item, "text"))


    # def print_selection(self,event):
    #      for selection in self.treeview.selection():
    #         item = self.treeview.item(selection)
    #         from_postcode, from_place, to_place = item["values"][0:3]
    #         text = "Selection: {}, {} <{}>"
    #         print(text.format(from_postcode,from_place, to_place))

    def create_treeview_widget(self, elf=None):

        columns = ("from postcode", "from place", "to place", "distance", "time", "date", "amount")
        print(columns[0])
        self.style = ttk.Style()
        self.style.theme_use("alt")
        # available theme names are ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
        self.style.configure("Treeview",background = 'D3D3D3',rowheight=25)
        self.style.map('Treeview',
                  background=[('selected','blue')])


        self.treeview = ttk.Treeview(self.frame, show="headings", columns=columns, height=18)
        self.treeview.heading('from postcode', text="from postcode")
        self.treeview.heading('from place', text="from place")
        self.treeview.heading('to place', text="to place")
        self.treeview.heading('distance', text="distance")
        self.treeview.heading('time', text="time")
        self.treeview.heading('date', text="date")
        self.treeview.heading('amount', text="amount")


        self.treeview.column(0, width=100)
        self.treeview.column(1, width=250)
        self.treeview.column(2, width=100)
        self.treeview.column(3, width=150)
        self.treeview.column(4, width=100)
        self.treeview.column(5, width=100)
        self.treeview.column(6, width=100)
        # add a scrollbar
        self.scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.treeview.yview)
        #self.scrollbar.pack()
        self.treeview.configure(yscrollcommand=self.treeview.set)
        self.scrollbar.pack
        self.scrollbar.config




        Data=self.get_data()
        email='cbelle.sharpe@gmail.com'
        for x in list(range(0, len(Data))):

            self.treeview.insert(parent='', index='0', iid=x,
                                     values=(Data[x][0], Data[x][1], Data[x][2], Data[x][3], Data[x][4], Data[x][5]))
            x += 1


        return self.treeview

    def new_window(self):
        self.win = tk.Toplevel(self)
        self.win.label = ttk.Label(self, text="Enter your email address: ")
        self.win.entry = ttk.Entry(self)
        self.frame=(self.Frame(self,"bg=pink"))
        self.frame.pack()
        self.app = MileageApp(self.newWindow)

#global variables
f = ('Times new roman', 18)


if __name__ == "__main__":
    app = MileageApp()
    app.mainloop()















