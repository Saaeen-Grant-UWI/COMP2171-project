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
        cursor.execute(f"INSERT INTO appointments (`date`, `time`, `payment_method`, `price`, `customer_id`, `status`, `attended`) VALUES ('{date}', '{time}', '{payment_method}', {price}, {customer}, 'active', 'no')")

        connection.commit()
        cursor.close()
        connection.close()

    
    def checkAppointments(self, date, time):
        connection = super().connect()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM appointments WHERE date = '{date}' AND time = '{time}' AND status = 'active';")
        query_result  = cursor.fetchall()

        cursor.close()
        connection.close()

        return query_result

    def updateAppointment(self,date, time, payment_method, appointment_id):
        connection = super().connect()
        cursor = connection.cursor(dictionary=True)
        # cursor.execute(f"INSERT INTO appointments (`date`, `time`, `payment_method`, `price`, `customer_id`, `status`) VALUES ('{date}', '{time}', '{payment_method}', {price}, {customer}, 'active')")
        cursor.execute(f"UPDATE appointments SET date = '{date}', time = '{time}', payment_method = '{payment_method}', status = 'active' WHERE id = {appointment_id};")

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
    
    def getAppointmentById(self, appointment_id):
        connection = super().connect()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(f"SELECT * FROM appointments where id = {appointment_id};")
        query_result = cursor.fetchall()

        cursor.close()
        connection.close()

        return query_result
    
    def getCustomerAppointment(self, customer):
        connection = super().connect()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM appointments WHERE customer_id = {customer};")
        query_result  = cursor.fetchall()

        cursor.close()
        connection.close()

        return query_result  
    
    def updateAppointmentSatus(self, status, appointment_id):
        connection = super().connect()
        cursor = connection.cursor()
        cursor.execute(f"UPDATE appointments SET status = '{status}' WHERE id = {appointment_id};")

        connection.commit()
        cursor.close()
        connection.close()

    def deleteAppointment(self, appointment_id):
        connection = super().connect()
        cursor = connection.cursor()
        cursor.execute(f"SET foreign_key_checks = 0; DELETE FROM appointments WHERE id = {appointment_id};", multi=True)

        connection.commit()
        cursor.close()
        connection.close()

    def getDateTime(self):
        connection = super().connect()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT id, date, time, status FROM appointments;")
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