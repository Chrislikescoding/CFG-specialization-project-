import tkinter as tk
import tkinter.ttk as ttk
from button_processor import SaveProcessor
from get_tree_data import get_tree_data
from PIL import ImageTk, Image


class MileageApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # create object, title and window size
        self.geometry('1000x800')
        self.configure(bg='white')
        self.title('CFG Specialization project')
        self.tree_frame = tk.Frame(self.master, bg='white')
        # self.cfg_image =Image.open("code-first-girls_image.png")
        # cfg_resized=self.cfg_image.resize((100, 100))
        # final_image=ImageTk.PhotoImage(cfg_resized)
        # self.plabel = ttk.Label(self.tree_frame,image=cfg_resized)
        # self.plabel.pack()

        self.label = ttk.Label(self.tree_frame, text="Py-miles ", foreground="white", background='#f54996',
                               font=bigf)
        self.label.pack()
        self.treeview = self.create_treeview_widget()
        self.frame2 = tk.Frame(self.master, bg='white')
        self.add_tree_frame = tk.Frame(self.master, bg='white')
        self.add_tree_frame2 = tk.Frame(self.master, bg='white')
        # #6 Label Widget
        self.label_submit = ttk.Label(self.add_tree_frame, text="Enter email address then Submit", font=littlef,
                                      background='#33FFA7')
        self.label_submit.pack(padx=5, pady=5, side=tk.LEFT)
        self.email_address = ttk.Entry(self.add_tree_frame, width=30, font=littlef)
        self.email_address.pack(padx=5, pady=5, side=tk.LEFT)
        self.save_processor = SaveProcessor(self.treeview)
        self.button2 = tk.Button(self.add_tree_frame, text='Submit Claim', bg='#f54996', fg='white',
                                 command=self.save_processor.button_action(), font=littlef)
        self.button2.pack(padx=5, pady=5, side=tk.LEFT)
        self.label_delete = ttk.Label(self.add_tree_frame, text="Select one or more lines then press delete",
                                      font=littlef, background='#33FFA7')
        self.label_delete.pack(padx=5, pady=5, side=tk.LEFT)
        self.del_rcd = tk.Button(self.add_tree_frame, text='Delete lines', bg='black', fg='white', font=littlef,
                                 command=self.del_rcd)
        self.del_rcd.pack(padx=5, pady=5, side=tk.RIGHT)
        self.label_email = ttk.Label(self.add_tree_frame2, text="Email_to_accounts", font=littlef,
                                     background='#33FFA7')
        self.label_email.pack(padx=5, pady=5, side=tk.LEFT)
        self.email_rcd = tk.Button(self.add_tree_frame2, text='Email', bg='#9b51e0', fg='white', font=littlef)
        #  command=self.cal_rcd)
        self.email_rcd.pack(padx=5, pady=5, side=tk.LEFT)
        self.label_calculate = ttk.Label(self.add_tree_frame2, text="Calculate expenses/add to database", font=littlef,
                                         background='#33FFA7')
        self.label_calculate.pack(padx=5, pady=5, side=tk.LEFT)
        self.cal_rcd = tk.Button(self.add_tree_frame2, text='Calculate', bg='#ffb930', fg='white', font=littlef)
        #  command=self.cal_rcd)
        self.cal_rcd.pack(padx=5, pady=5, side=tk.LEFT)
        self.label_statistics = ttk.Label(self.add_tree_frame2, text="Display statistics", font=littlef,
                                          background='#33FFA7')
        self.label_statistics.pack(padx=5, pady=5, side=tk.LEFT)
        self.cal_rcd = tk.Button(self.add_tree_frame2, text='Statistics', bg='#00bbf9', fg='white', font=littlef)
        #  command=self.cal_rcd)
        self.cal_rcd.pack(padx=5, pady=5, side=tk.LEFT)
        self.tree_frame.pack(pady=20)
        self.add_tree_frame.pack(pady=20)
        self.add_tree_frame2.pack(pady=20)
        self.frame2.pack()

    def del_rcd(self):
        x = self.treeview.selection()
        for record in x:
            self.treeview.delete(record)

    def create_treeview_widget(self, elf=None):
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
        Data = get_tree_data(self)
        email = 'cbelle.sharpe@gmail.com'
        self.treeview.tag_configure('evenrow', background='#00bbf9')
        self.treeview.tag_configure('oddrow', background='white')
        for x in list(range(0, len(Data))):
            if x % 2 == 0:
                self.treeview.insert(parent='', index='0', iid=x,
                                     values=(Data[x][0], Data[x][1], Data[x][2], Data[x][3], Data[x][4], Data[x][5]),
                                     tags=('evenrow',))
            else:
                self.treeview.insert(parent='', index='0', iid=x,
                                     values=(Data[x][0], Data[x][1], Data[x][2], Data[x][3], Data[x][4], Data[x][5]),
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