import mysql.connector as mysql
from mysql.connector import Error

class Database():

    my_db = my_cursor = None

    def __init__(self):
        global my_db, my_cursor
        my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Smudge03!",
            database="Persons"
        )
        my_cursor = my_db.cursor()

    def __del__(self):
        my_db.commit()

    # Connect to the database
    def _connect_to_db(db_name):
        cnx = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=db_name
        )
        return cnx

    # EXAMPLE 1, get all records from db
    # SELECT * FROM abcreport
    def get_all_records():
        try:
            db_name = 'tests'
            db_connection = _connect_to_db(db_name)
            cur = db_connection.cursor()
            print(f"Connected to DB: {db_name}")

            query = "SELECT * FROM abcreport"
            cur.execute(query)
            result = cur.fetchall()  # a list with db records, where each record is a tuple

            for record in result:
                print(record)

            cur.close()

        except Exception:
            raise DbConnectionError("Failed to read data from DB")

        finally:
            if db_connection:
                db_connection.close()
                print("DB connection is closed")



