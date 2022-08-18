from database_connect import *
import Person


class PersonClaimsProcessor:
    # The single responsibility of this class is to retrieve the claim records,
    # these records were mocked in the database
    # we will retrieve the amount claimed this month and the total claimed so far,
    # these amounts will be used to determine the
    # amount calculations later on

    #    def get_person_records(self):
    def get_total_claimed(self):
        return int(self.total_claimed)

    def claimed_this_month(self):
        print(f'self.claimed_this_month')
        return int(self.claimed_this_month)

    def get_claim_records(self):
        db_connection = None
        try:
            db_name = 'Person'
            db_connection = connect_to_db(db_name)
            cur = db_connection.cursor()
            print("Connected to DB: %s" % db_name)
            query = "SELECT claimed_this_month, total_claimed from PersonClaims as c " \
                    "where c.email_address= 'CBelle.Sharp@gmail.com'"
            cur.execute(query)
            result = cur.fetchone()  # a list with db records, where each record is a tuple
            self.claimed_this_month = result[0]
            self.total_claimed = result[1]
        except Exception:
            raise DbConnectionError("Failed to read data from DB")

        finally:
            cur.close()
            print("DB connection is closed")
