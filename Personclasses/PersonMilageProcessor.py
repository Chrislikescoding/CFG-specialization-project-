from database_connect import *


class PersonMilageProcessor:
    # The single responsibility of this class is to retrieve the mileage for
    # this month for the person object instantiated by the person class
    def __init__(self, email_address):
        self.email_address = email_address

    def get_mileage(self):
        return self.this_month_miles

    def get_this_month_miles(self):
        email_address = self.email_address
        result = None
        db_connection = None
        try:
            db_name = 'Person'
            db_connection = connect_to_db(db_name)
            cur = db_connection.cursor()
            print("Connected to DB: %s" % db_name)
            query = "SELECT sum(miles) from Mileage WHERE email_address=email_address"
            cur.execute(query)
            result = cur.fetchone()  # a list with db records, where each record is a tuple
            self.this_month_miles = result[0]
            print(type(self.this_month_miles))
        except Exception:
            raise DbConnectionError("Failed to read data from DB")

        finally:
            cur.close()
            print("DB connection is closed")
