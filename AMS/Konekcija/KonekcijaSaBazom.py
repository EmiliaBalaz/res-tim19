import mysql.connector
from mysql.connector import Error

def konekcijaBaze(upit, vrednosti):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='AMS',
                                             user='emily',
                                             password='10042001')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute(upit, vrednosti)
            record = cursor.fetchone()
            connection.commit()
            print("You're connected to database: ", record)
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


