class Employee():#Employee also includes self employed person       :
    # Constructor method to initialize object
    def __init__(self, name=" ",job_title= "", post_code = " " ,email_address =" ", emp_total= 0):
        # initialize attributes
        self.name = name
        self.job_title = job_title
        self.post_code = post_code
        self.email_address=email_address


    def set_home(self,post_code):
        # Call from GUI to use to  hide the home address on csv file
        def home_postcode(self, post_code):
            self.postcode = post_code

        # Call from GUI to use to  hide the home address on csv file
    def set_home_postcode(self, post_code):
        self.postcode = post_code

employee_first = Employee("Chris", "software engineer","LN4 3AW", "Cbelle.sharp@gmail.com",10000)

# Class blueprint for a Tiger
# Inherit from Cat
class EmployeeClaimHistory(Employee):
    # If the child class initializes differently, use super() to initialize the base class first
    def __init__(self, name, job_title, post_code,email_address, previous_claimed_month,total_claimed ):
        super().__init__( name, job_title, post_code, email_address)
        # we need to locate the google history file name for this employee
   #     self.path_to_google_history_file = path_to_google_history_file
   #     self.google_history_file_name = google_history_file_name
        self.__total_claimed = total_claimed
        self.previous_claimed_month = previous_claimed_month
    # To be set from month and employee name

    def set_history_filename(self):
        pass
    def set_path(self):
        pass

    def set_claim_amount(self,amount):
        return amount * 0.45

    def decide_rate(self,__total_claimed):
        if __total_claimed < 10000:
            rate = .45
        else:
            rate = .25

    def accumulate_total(fnc):
        def inner():
          return fnc()

        return inner

    @accumulate_total
    def multiply_miles_by_rate(self,miles,rate):
        return (miles * rate)



if __name__ == '__main__':
    employee_info = EmployeeClaimHistory("Chris", "software engineer", 'LN4,3AW', "sharpchr@gmail.com", "c:", "first", 10000)
    employee_info.multiply_miles_by_rate()