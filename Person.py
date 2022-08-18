from database_connect import *

# The object of the person class is to initialise a person and check whether that person exists in the database.
# SOLID = Single use - validation of the person only
class Person():
# Constructor method to initialize object
    def __init__(self,  email_address=" "):
        # initialize attributes
        self.email_address = email_address


#intention here is to capture the home postcode and for future versions set it to "Home" for privacy reasons
    @property
    def home(self):
        return self._home_postcode
    @home.setter
    def home(self, home_postcode):
        if isinstance(home_postcode, str):
            self._home_postcode = home_postcode
        else:
            raise AttributeError("no home postcode")

# SELECT * FROM Person table on the database to check if the person with the email passed in via the GUI exists
    def get_person_records(self):
        result = None
        db_connection = None
        try:
            db_name = 'Person'
            db_connection = connect_to_db(db_name)
            cur = db_connection.cursor()
            print("Connected to DB: %s" % db_name)
            query = "SELECT postcode from Persons as p where p.email_address= 'CBelle.Sharp@gmail.com'";
            cur.execute(query)
# if the record exists then set the home postcode - this was set up so that in future versions the home postcode can be set as "Home" to hide location
            row=cur.fetchone()
            home_postcode=(row[0])
        except Exception:
            raise DbConnectionError("Failed to read data from DB")

        finally:
            cur.close()
            print("DB connection is closed")
#         print("1")
# first_person = Person("Chris", "tech department", "LN4 3AW", "Cbelle.sharp@gmail.com")
# first_person.get_person_records()