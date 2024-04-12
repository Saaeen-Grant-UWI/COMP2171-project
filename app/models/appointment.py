from .database import Database

class Appointment(Database):
    
    def getAppointments(self):
        connection = super().connect()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('select * from appointments')
        query_result  = cursor.fetchall()

        cursor.close()
        connection.close()

        return query_result
    
    def insertAppointment(self,date, time, payment_method, price, customer):
        connection = super().connect()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"INSERT INTO appointments (`date`, `time`, `payment_method`, `price`, `customer_id`) VALUES ('{date}', '{time}', '{payment_method}', {price}, {customer})")

        connection.commit()
        cursor.close()
        connection.close()
    
    def getLastAppointmentId(self):
        connection = super().connect()
        cursor = connection.cursor(dictionary=True)
        query_result = []

        cursor.execute(f"SELECT id FROM appointments ORDER BY id DESC LIMIT 1;")
        temp = cursor.fetchall()

        if(temp):
            query_result = temp[0]["id"]
        else:
            query_result = 0

        cursor.close()
        connection.close()

        return int(query_result)
    
    def getCustomerAppointment(self, customer):
        connection = super().connect()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM appointments WHERE customer_id = {customer};")
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