import csv
import load_mileage_file
def submit_claim(self):
    #  use the data from treeview to create the monthly csv claim file here
    with open("new_monthly_claim.csv", "w", newline='') as myfile:
        print("saving your claim data")
        csvwriter = csv.writer(myfile, delimiter=',')
        for row_id in self.treeview.get_children():
            row = self.treeview.item(row_id)['values']
            csvwriter.writerow(row)

load_mileage_file
