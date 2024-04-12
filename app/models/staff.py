from .database import Database

class Staff(Database):
    
    def getStaff(self):
        connection = super().connect()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('select * from staff')
        query_result  = cursor.fetchall()

        cursor.close()
        connection.close()

        return query_result
    
    def insertStaff(self,staff, appointment):
        connection = super().connect()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"INSERT INTO booked_staff (`staff_id`, `appointment_id`) VALUES ({staff}, {appointment})")

        connection.commit()
        cursor.close()
        connection.close()
    
    
    def getStaffWhereAnd(self, rating, specialization):
        connection = super().connect()
        cursor = connection.cursor(dictionary=True)


        cursor.execute(f"SELECT * FROM staff WHERE rating = {rating} AND type = '{specialization}';")
        query_result  = cursor.fetchall()

        cursor.close()
        connection.close()

        return query_result  
    
    def getStaffWhere(self,search, data):
        connection = super().connect()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"select * from staff where {search} = '{data}' ")
        query_result  = cursor.fetchall()

        cursor.close()
        connection.close()

        return query_result  
    
    # def insertUser(self,username, password):
    #     connection = super().connect()
    #     cursor = connection.cursor(dictionary=True)
    #     cursor.execute(f"INSERT INTO users (`username`, `password`, `type`) VALUES ('{username}', '{password}', 'customer')")

    #     connection.commit()
    #     cursor.close()
    #     connection.close()