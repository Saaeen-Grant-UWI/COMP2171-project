from .database import Database

class Service(Database):
    
    def getServices(self):
        connection = super().connect()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('select * from services')
        query_result  = cursor.fetchall()

        cursor.close()
        connection.close()

        return query_result
    
    def insertService(self, service, appointment):
        connection = super().connect()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO booked_services (`service_id`, `appointment_id`) VALUES ({service}, {appointment})")

        connection.commit()
        cursor.close()
        connection.close()
    
    def bookedDelete(self, appointment_id):

        connection = super().connect()
        cursor = connection.cursor()

        cursor.execute(f"DELETE FROM booked_services WHERE appointment_id = {appointment_id};")

        connection.commit()
        cursor.close()
        connection.close()
    # def getUserById(self, data):
    #     connection = super().connect()
    #     cursor = connection.cursor(dictionary=True)
    #     cursor.execute(f"select * from users where id = {data}")
    #     query_result  = cursor.fetchall()

    #     cursor.close()
    #     connection.close()

    #     return query_result  
    
    # def getUserWhere(self,search, data):
    #     connection = super().connect()
    #     cursor = connection.cursor(dictionary=True)
    #     cursor.execute(f"select * from users where {search} = '{data}' ")
    #     query_result  = cursor.fetchall()

    #     cursor.close()
    #     connection.close()

    #     return query_result  
    
    # def insertUser(self,username, password):
    #     connection = super().connect()
    #     cursor = connection.cursor(dictionary=True)
    #     cursor.execute(f"INSERT INTO users (`username`, `password`, `type`) VALUES ('{username}', '{password}', 'customer')")

    #     connection.commit()
    #     cursor.close()
    #     connection.close()