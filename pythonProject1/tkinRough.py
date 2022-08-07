from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
import os
from os.path import exists, join


#2 create object, title and window size
ws = Tk()
ws.title('Office Expense')
# ws.geometry('600x400')

#4 global variables
f = ('Times new roman', 18)
amtvar = IntVar()
dopvar = StringVar()

#5 frame widgets
f2 = Frame(ws)
f2.pack()

f1 = Frame(
    ws,
    padx=10,
    pady=10,
)
f1.pack(expand=True, fill=BOTH)


#6 Label Widget
Label(f1, text='ITEM NAME', font=f).grid(row=0, column=0, sticky=W)
Label(f1, text='ITEM PRICE', font=f).grid(row=1, column=0, sticky=W)
Label(f1, text='PURCHASE DATE', font=f).grid(row=2, column=0, sticky=W)

#7 Entry Widgets
item_name = Entry(f1, font=f)
item_amt = Entry(f1, font=f, textvariable=amtvar)
transaction_date = Entry(f1, font=f, textvariable=dopvar)


#8 Entry grid placement
item_name.grid(row=0, column=1, sticky=EW, padx=(10, 0))
item_amt.grid(row=1, column=1, sticky=EW, padx=(10, 0))
transaction_date.grid(row=2, column=1, sticky=EW, padx=(10, 0))


#9 Action buttons
cur_date = Button(
    f1,
    text='Current Date',
    font=f,
    bg='#04C4D9',
    command=None,
    width=15
    )

submit_btn = Button(
    f1,
    text='Save Record',
    font=f,
    command=None,
    bg='#42602D',
    fg='white'
    )

clr_btn = Button(
    f1,
    text='Clear Entry',
    font=f,
    command=None,
    bg='#D9B036',
    fg='white'
    )

quit_btn = Button(
    f1,
    text='Exit',
    font=f,
    command=None,
    bg='#D33532',
    fg='white'
    )

total_bal = Button(
    f1,
    text='Total Balance',
    font=f,
    command=None
)

total_bal = Button(
    f1,
    text='Total Balance',
    font=f,
    bg='#486966',
    fg='white',
    command=None
)

total_spent = Button(
    f1,
    text='Total Spent',
    font=f,
    fg='white',
    command=None
)

update_btn = Button(
    f1,
    text='Update',
    bg='#C2BB00',
    command=None,
    fg='white',
    font=f
)

del_btn = Button(
    f1,
    text='Delete',
    bg='#BD2A2E',
    fg='white',
    command=None,
    font=f
)

#10 Button grid placement
cur_date.grid(row=3, column=1, sticky=EW, padx=(10, 0))
submit_btn.grid(row=0, column=2, sticky=EW, padx=(10, 0))
clr_btn.grid(row=1, column=2, sticky=EW, padx=(10, 0))
quit_btn.grid(row=2, column=2, sticky=EW, padx=(10, 0))
total_bal.grid(row=0, column=3, sticky=EW, padx=(10, 0))
update_btn.grid(row=1, column=3, sticky=EW, padx=(10, 0))
del_btn.grid(row=2, column=3, sticky=EW, padx=(10, 0))

#11 treeview to view the record
tv = ttk.Treeview(f2, selectmode='browse', columns=(1, 2, 3, 4), show='headings', height=8, )
tv.pack(side="left")

tv.column(1, anchor=CENTER, stretch=NO, width=50)
tv.column(2, anchor=CENTER)
tv.column(3, anchor=CENTER)
tv.column(4, anchor=CENTER)
tv.heading(1, text="Serial no")
tv.heading(2, text="Item Name", )
tv.heading(3, text="Item Price")
tv.heading(4, text="Purchase Date")

style = ttk.Style()
style.theme_use("default")
style.map("Treeview")

path = os.getcwd()
print(path)
path: str=join(path, 'first.csv')
File = open(str(path))
Reader = csv.reader(File)
Data = list(Reader)
del Data[0]


entries = []
for x in list(range(0, len(Data))):
	tv.insert(parent='', index='0', iid=x, values=(Data[x][0], Data[x][1],Data[x][2], Data[x][3]))
	x+= 1
#	tv.after(400, refreshData)

  #  entries.append(Data[x][0])

#for entry in entries:
 #       tv.insert(parent='', index='0', iid=count, values=(rec[0], rec[1], rec[2], rec[3]))


#12 scrollbar widget
scrollbar = Scrollbar(f2, orient='vertical')
scrollbar.configure(command=tv.yview)
scrollbar.pack(side="right", fill="y")
tv.config(yscrollcommand=scrollbar.set)


#3 infinite loop
ws.mainloop()

