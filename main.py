# build a GUI- please note that this is MAC specific as the Windows developed version did not work
# on the MAC tkmacosx and tkm are the MAC specific pieces of code
import tkinter as tk
import tkinter.ttk as ttk
import tkmacosx as tkm
from get_tree_data import get_tree_data
from submit_claim import submit_claim


class MileageApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # create object, title and window size
        self.geometry('1000x800')
        self.configure(bg='white')
        self.title('CFG Specialization project')
        self.tree_frame = tk.Frame(self.master, bg='white')
        self.label = ttk.Label(self.tree_frame, text="Py-miles ", foreground="white", background='#f54996',
                               font=bigf)
        self.label.pack()
        # create the treeview
        self.treeview = self.create_treeview_widget()
        self.frame2 = tk.Frame(self.master, bg='white')
        self.add_tree_frame = tk.Frame(self.master, bg='white')
        self.add_tree_frame2 = tk.Frame(self.master, bg='white')
        #  add labels and buttons
        self.label_submit = ttk.Label(self.add_tree_frame, text="Enter email address then Submit", font=littlef,
                                      background='#33FFA7')
        self.label_submit.pack(padx=5, pady=5, side=tk.LEFT)
        self.email_address = ttk.Entry(self.add_tree_frame, width=30, font=littlef)
        self.email_address.pack(padx=5, pady=5, side=tk.LEFT)
        self.button2 = tkm.Button(self.add_tree_frame, text='Submit Claim', background='#f54996', fg='white',
                                 command=submit_claim(self), font=littlef)
        self.button2.pack(padx=5, pady=5, side=tk.LEFT)
        self.label_delete = ttk.Label(self.add_tree_frame, text="Select one or more lines then press delete",
                                      font=littlef, background='#33FFA7')
        self.label_delete.pack(padx=5, pady=5, side=tk.LEFT)
        self.del_rcd = tkm.Button(self.add_tree_frame, text='Delete lines', background='black',
                                  fg='white', font=littlef, command=self.del_rcd)
        self.del_rcd.pack(padx=5, pady=5, side=tk.RIGHT)
        self.label_email = ttk.Label(self.add_tree_frame2, text="Email_to_accounts", font=littlef,
                                     background='#33FFA7')
        self.label_email.pack(padx=5, pady=5, side=tk.LEFT)
        self.email_rcd = tkm.Button(self.add_tree_frame2, text='Email', background='#9b51e0', fg='white', font=littlef)

        self.email_rcd.pack(padx=5, pady=5, side=tk.LEFT)
        # pack it all in
        self.tree_frame.pack(pady=20)
        self.add_tree_frame.pack(pady=20)
        self.add_tree_frame2.pack(pady=20)
        self.frame2.pack()
    # function to delete treeview records

    def del_rcd(self):
        x = self.treeview.selection()
        for record in x:
            self.treeview.delete(record)

    # create the  treeview records
    def create_treeview_widget(self):
        # build treeview columns
        columns = ("from postcode", "from place", "to place", "distance", "time", "date", "amount")
        print(columns[0])
        self.style = ttk.Style()
        self.style.theme_use("alt")
        # available theme names are ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
        self.style.configure("Treeview", background='white', rowheight=20)
        self.style.map('Treeview',
                       background=[('selected', 'pink')])
        self.treeview = ttk.Treeview(self.tree_frame, show="headings", columns=columns, height=25)
        self.treeview.pack()
        # build treeview headings
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
        data = get_tree_data(self)
        self.treeview.tag_configure('evenrow', background='#00bbf9')
        self.treeview.tag_configure('oddrow', background='white')
# use the csv data and make a stripy treeview! :)
        for x in list(range(0, len(data))):
            if x % 2 == 0:
                self.treeview.insert(parent='', index='0', iid=x,
                                     values=(data[x][0], data[x][1], data[x][2], data[x][3], data[x][4], data[x][5]),
                                     tags=('evenrow',))
            else:
                self.treeview.insert(parent='', index='0', iid=x,
                                     values=(data[x][0], data[x][1], data[x][2], data[x][3], data[x][4], data[x][5]),
                                     tags=('oddrow',))
            x += 1
        return self.treeview


# global variables
littlef = ('Times new roman', 12)
f = ('Times new roman', 18)
bigf = ('Times new roman', 24)

if __name__ == "__main__":
    app = MileageApp()
    app.mainloop()
