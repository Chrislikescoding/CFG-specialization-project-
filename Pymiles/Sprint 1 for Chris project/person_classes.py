class Person():#Employee also includes self employed person       :
    # Constructor method to initialize object
    def __init__(self,  email_address=" ",department= "", first_name = "", last_name = "", address = "",post_code = ""):
        # initialize attributes
        self.email_address = email_address
        self.department = department
        self.first_name = first_name
        self.last_name = last_name
        self.post_code = post_code
        self.address=address

    def set_home(self,post_code):
        # Call from GUI to use to  hide the home address on csv file
        def home_postcode(self, post_code):
            self.postcode = post_code


employee_first = Person("Chris", "software engineer","LN4 3AW", "Cbelle.sharp@gmail.com")

# Class blueprint for a Tiger
# Inherit from Cat
class PersonClaim(Person):
    # If the child class initializes differently, use super() to initialize the base class first
    def __init__(self, email_address,department , first_name  , last_name  , address  ,post_code,total_claimed):
        super().__init__( email_address,department , first_name  , last_name  , address  ,post_code  )
        # we need to locate the google history file name for this employee
      #  self.path_to_google_history_file = path_to_google_history_file
     #   self.google_history_file_name = google_history_file_name
    # To be set from month and employee name

    def set_history_filename(self):
        pass
    def set_path(self):
        pass

#calcs
# get amounts total claimed and current claimed amount
# to calculate this months claimed, then move the current to last months claimed before updatinf
# claim to be able to work out amoutrson

#use SQL to select the person with the same email address from persons file, match it to the file we are sending through
# calculate the total claimed anmount - so if claim amount is LT 10000 x.45 and add on the milage
#                                       if claim reaches 10,000 split and calculate x .25
# keep running total of THIS amount claimed and total amount claimed
# update the record check the Bank account classes out
