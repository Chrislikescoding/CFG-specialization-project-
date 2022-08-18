import matplotlib.pyplot as plt
from database_connect import *
# class to catch connection errors


class ExpensesStats:

    def get_records(self):
        result = None
        db_connection = None
        try:
            db_name = 'Person'
            db_connection = connect_to_db(db_name)
            cur = db_connection.cursor()
            print("Connected to DB: %s" % db_name)
            query = "SELECT p.person_name,c.claimed_this_month from Persons as p inner join Personclaims as c" \
                    " on p.email_address = c.email_address "

            cur.execute(query)
            result = cur.fetchall
            # a list with db records, where each record is a tuple
            names = []
            monthly_claims = []

            for x in cur:
                names.append(x[0][0:10])
                monthly_claims.append(x[1])

            plt.bar(names, monthly_claims)
            plt.ylim(0, 5000)
            plt.xlabel("email address")
            plt.ylabel("employee claims")
            plt.title("claim amounts this month")
            plt.show()
            plt.waitforbuttonpress(0)
        except Exception as e:
            print(e)
            plt.close('all')
        finally:
            plt.close('all')
            print("DB connection is closed")


expenses_stats = ExpensesStats()
expenses_stats.get_records()
