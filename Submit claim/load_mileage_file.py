import csv
import mysql.connector
from database_connect import *


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


def db_add_csv(postcode, place_from, place_to, metres):

    db_connection = None
    try:
        db_name = 'Person'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)
        email_address = 'CBelle.sharpe@gmail.com'
        query = """
            INSERT INTO Mileage (email_address,postcode_from,place_from,place_to,miles)
            VALUES (%s,%s, %s, %s,%s)
            """
        data = (email_address, postcode, place_from, place_to, miles)
        cur.execute(query, data)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def metres_to_miles(metres):
    calculated_miles = int(metres) * 0.000621371
    return int(calculated_miles)


file = 'new_monthly_claim.csv'


with open(file,
          "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    print(csv_reader)

    for row in csv_reader:
        email = 'CBelle.sharpe@gmail.com'
        try:
            metres = (row[3])
            miles = metres_to_miles(int(metres))
            db_add_csv(row[0], row[1], row[2], miles)
        except Exception as e:
            print(e)
