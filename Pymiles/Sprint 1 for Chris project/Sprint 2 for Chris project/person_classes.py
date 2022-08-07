import mysql.connector
from config import USER, HOST, PASSWORD
# Exception
class DbConnectionError(Exception):
    pass

class Database():
    my_db = my_cursor = None

    def __init__(self):
        global my_db, my_cursor
        my_db = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database="Person"
        )
        my_cursor = my_db.cursor()

    def __del__(self):
        my_db.commit()


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


    # SELECT * FROM Person
    def get_person_records(self):
        try:
            query = "SELECT postcode from Persons as p where p.email_address= 'CBelle.Sharp@gmail.com'";
            my_cursor.execute(query)
            result = my_cursor.fetchall()  # a list with db records, where each record is a tuple

            for record in result:
                print(record)

            my_cursor.close()

        except Exception:
            raise DbConnectionError("Failed to read data from DB")

        finally:
            if my_db:
                my_db.close()
                print("DB connection is closed")


    def set_home(self,post_code):
        # Call from GUI to use to  hide the home address on csv file
        def home_postcode(self, post_code):
            self.postcode = post_code


employee_first = Person("Chris", "software engineer","LN4 3AW", "Cbelle.sharp@gmail.com")
database=Database()
employee_first.get_person_records()

# Class blueprint for a Tiger
# Inherit from Cat
class PersonClaim(Person):
    # If the child class initializes differently, use super() to initialize the base class first
    def __init__(self, email_address):
        self.email_address = email_address


    def get_claim_records(self):
        try:
            query = "SELECT claimed_this_month, total_claimed from PersonClaims as c where c.email_address= 'CBelle.Sharp@gmail.com'";
            my_cursor.execute(query)
            result = my_cursor.fetchall()  # a list with db records, where each record is a tuple

            for record in result:
                print(record)

            my_cursor.close()

        except Exception:
            raise DbConnectionError("Failed to read data from DB")

        finally:
            if my_db:
                my_db.close()
                print("DB connection is closed")

    def get_this_month_miles(self):
        try:
            query = "SELECT sum(miles) from Mileage";
            my_cursor.execute(query)
            result = my_cursor.fetchall()  # a list with db records, where each record is a tuple

            for record in result:
                print(record)

            my_cursor.close()

        except Exception:
            raise DbConnectionError("Failed to read data from DB")

        finally:
            if my_db:
                my_db.close()
                print("DB connection is closed")



person_claim = PersonClaim("Cbelle.sharp@gmail.com")
database = Database()
person_claim.get_this_month_miles()

person_claim = PersonClaim("Cbelle.sharp@gmail.com")
database = Database()
person_claim.get_claim_records()
#person_claim.calculate()











#calcs
# get amounts total claimed and current claimed amount
# to calculate this months claimed, then move the current to last months claimed before updatinf
# claim to be able to work out amoutrson

#use SQL to select the person with the same email address from persons file, match it to the file we are sending through
# calculate the total claimed anmount - so if claim amount is LT 10000 x.45 and add on the milage
#                                       if claim reaches 10,000 split and calculate x .25
# keep running total of THIS amount claimed and total amount claimed
# update the record check the Bank account classes out
