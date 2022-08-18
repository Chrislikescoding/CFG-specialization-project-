import tkinter as tk
import tkmacosx as tkm
import db_calculation_func
# This is a GUI to do the functions on the accounts payable or accountant side i.e. the person who checks
# the expense claim,makes the calculations, and adds it to the database
from CalculateExpenses import CalculateExpenses
from Person import Person
from PersonClaimsProcessor import PersonClaimsProcessor
from PersonClaimsUpdater import PersonClaimsUpdater
from PersonMilageProcessor import PersonMilageProcessor
from expenses_stats import expenses_stats


class DbUpdateApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('800x300')
        self.configure(bg='white')
        self.title('CFG Specialization project')
        # add labels and buttons
        self.frame1 = tk.Frame(self.master, bg='white')
        self.frame2 = tk.Frame(self.master, bg='white')
        self.frame3 = tk.Frame(self.master, bg='white')
        self.label = tk.Label(self.frame1, text="Py-miles Accounts Department", foreground="white", bg='#f54996',
             font=bigf)
        self.label.pack(ipadx=10, ipady=10)
        self.frame1.pack()
        self.label_instr = tk.Label(self.frame2, text="Pressing the calculate button will"
        " calculate expenses/add to database", font=f, bg='#ffb930')
        self.label_instr.pack(ipadx=10, ipady=10, side='left')

        #  button to calculate the expense claim
        self.cal_rcd = tkm.Button(self.frame2, text='Calculate', background='#9b51e0', fg='white', font=bigf,
        command = self.db_calculation)
        self.cal_rcd.pack(ipadx=10, ipady=10, side='right')
        self.frame2.pack()
        self.label_instr = tk.Label(self.frame3, text="Pressing the Display Statistics button will display "
        "the claim statistics for this months claims", font=f, background='#ffb930')

        self.label_instr.pack(ipadx=10, ipady=10, side='left')

        #  button to calculate the expense stats - currently disabled because the window wont go away!
        self.stat_rcd = tkm.Button(self.frame3, text='Statistics', background='#00bbf9', fg='white', font=bigf,
        command=expenses_stats.get_records())
        self.stat_rcd.pack(ipadx=10, ipady=10, side='right')
        self.frame3.pack()

    def db_calculation(self):
        first_person = Person("Cbelle.sharpe@gmail.com")
        first_person.get_person_records()
        person_claim = PersonClaimsProcessor()
        person_claim.get_claim_records()
        print("Got ya!!!")
        person_milage = PersonMilageProcessor("Cbelle.sharp@gmail.com")
        person_milage.get_this_month_miles(first_person)
        miles_this_claim = person_milage.get_mileage()
        total_miles_claimed = person_claim.get_total_claimed()
        calculate_expenses = CalculateExpenses(total_miles_claimed, miles_this_claim)
        amount = calculate_expenses.calculate()
        person_update_claim = PersonClaimsUpdater(amount, miles_this_claim)
        person_update_claim.update_records()


# global variables
littlef = ('Times new roman', 12)
f = ('Times new roman', 18)
bigf = ('Times new roman', 24)
if __name__ == "__main__":
    app = DbUpdateApp()
    app.mainloop()
