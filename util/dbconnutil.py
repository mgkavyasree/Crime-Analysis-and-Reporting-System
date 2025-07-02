import mysql.connector

class DBConnUtil:
    @staticmethod
    def getconnection():
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="kavya",
                database="crime_db"
            )
            if connection.is_connected():
                print("Database connection established successfully.")
            return connection
        except mysql.connector.Error as err:
            print(f"Error: Could not connect to the database. {err}")
            return None
