from database_connect import *


class PersonClaimsUpdater:
    def __init__(self, calculated_amount, miles_this_claim):
        # initialize attributes
        self.calculated_amount = calculated_amount
        self.miles_this_claim = miles_this_claim
        print(type(calculated_amount))
        print(type(self.miles_this_claim))
# The single responsibility of this class is to update the claim records
# update is: claimed this month becomes claimed last month,
#            claimed this_month will be the calculated amount
#            new total amount will be total amount + claimed this_month
#            total miles will be total miles + miles this month

    def update_records(self):
        db_connection = None
        try:
            print("4")
            db_name = 'Person'
            db_connection = connect_to_db(db_name)
            cur = db_connection.cursor()
            print("Connected to DB: %s" % db_name)
            query = "UPDATE	Personclaims SET claimed_last_month=claimed_this_month,claimed_this_month = %s," \
                    "total_claimed = total_claimed + %s,total_miles=total_miles+%s " \
                    "WHERE email_address='cbelle.sharp@gmail.com'"

            cur.execute(query, (self.calculated_amount, self.calculated_amount, self.miles_this_claim))

        except Exception:
            raise DbConnectionError("Failed to UPDATE data from DB")

        finally:
            db_connection.commit()
            cur.close()
            print("DB connection is updated")
            print("DB connection is closed")
