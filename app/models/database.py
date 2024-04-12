import mysql.connector


class Database():
    
    def connect(self):
        
        SERVER_NAME = "localhost"
        USERNAME = "root"
        PASSWORD = ""
        DATABASE = "arc_db"

        return mysql.connector.connect( host = SERVER_NAME, user = USERNAME , password = PASSWORD, database = DATABASE,)


