from .database import Database

class User(Database):
    
    def getUsers(self):
        connection = super().connect()
        cursor = connection.cursor()
        cursor.execute('select * from users')
        query_result  = cursor.fetchall()

        cursor.close()
        connection.close()

        return query_result
    
    def getUserById(self, data):
        connection = super().connect()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"select * from users where id = {data}")
        query_result  = cursor.fetchall()

        cursor.close()
        connection.close()

        return query_result  
    
    def getUserWhere(self,search, data):
        connection = super().connect()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"select * from users where {search} = '{data}' ")
        query_result  = cursor.fetchall()

        cursor.close()
        connection.close()

        return query_result  
    
    def insertUser(self,username, password):
        connection = super().connect()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"INSERT INTO users (`username`, `password`, `type`) VALUES ('{username}', '{password}', 'customer')")

        connection.commit()
        cursor.close()
        connection.close()