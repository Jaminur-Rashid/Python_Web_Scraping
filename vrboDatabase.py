#################
# This script creates a database table
# named as vrbo_hotel_info_table in the database
# Author : Jaminur Rashid
# Data   : 8-12-2021
##################
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="vrboDatabase"
)

# Creating vrbo database

cursor = mydb.cursor()
print("Ok")
try:
    #cursor.execute("CREATE DATABASE vrboDatabase")
    #print("vrbo Database Created")
    mySql_Create_Table_Query = """CREATE TABLE vrbo_hotel_info_table ( 
                                 Id varchar(100) NOT NULL,
                                 Location varchar(100) NOT NULL,
                                 Hotel_Name varchar(100) NOT NULL,
                                 Sleeping varchar(20) NOT NULL,
                                 Bedroom varchar(20) NOT NULL,
                                 Bathroom varchar(20) NOT NULL,
                                 Price varchar(20) NOT NULL,
                                 PRIMARY KEY (Hotel_Name)) """
    print("Vrbo_Hotel_Table Created Successfully")
    result = cursor.execute(mySql_Create_Table_Query)
except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("MySQL connection is closed")


def check():
    print("I am from check.py")