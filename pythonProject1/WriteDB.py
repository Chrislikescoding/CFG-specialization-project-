import pandas as pd
impdata = pd.read_csv('first.csv', index_col=False, delimiter = ',')
impdata.head()

import mysql.connector as msql
from mysql.connector import Error
#try:
conn = msql.connect(host='localhost', user='root',
                    password='Smudge03!')#give ur username, password
if conn.is_connected():
    cursor = conn.cursor()
   # cursor.execute("CREATE DATABASE employeee")
  #  print("Database is created")
  #  cursor.execute(
    #    "CREATE TABLE employeee2_data(place_name varchar(255),address varchar(255),start_time varchar(8),end_time varchar(8),distance float(10))")
  #  print("Table is created....")
    # loop through the data frame
    for i, row in impdata.iterrows():
        # here %S means string values
        sql = "INSERT INTO employeee.employeee_data VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sql, tuple(row))
        print("Record inserted")
        # the connection is not auto committed by default, so we must commit to save our changes
        conn.commit()
#except Error as e:
   # print("Error while connecting to MySQL", e)





