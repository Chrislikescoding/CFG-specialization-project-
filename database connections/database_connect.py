import mysql.connector
from config import USER, HOST, PASSWORD


class DbConnectionError(Exception):
    pass


def connect_to_db(db_name):

    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx
