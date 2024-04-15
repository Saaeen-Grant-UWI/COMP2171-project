from datetime import datetime, timedelta
from .database import Database

class Calender():
    
    @staticmethod
    def getWeek():
        def get_current_week_dates():
            today = datetime.today().date()  # Get the current date without time
            start_of_week = today - timedelta(days=today.weekday())
            end_of_week = start_of_week + timedelta(days=6)
            return start_of_week, end_of_week

        def get_dates_between(start_date, end_date):
            dates = []
            current_date = start_date
            while current_date <= end_date:
                dates.append(current_date.strftime("%Y-%m-%d"))
                current_date += timedelta(days=1)
            return dates

        start_date, end_date = get_current_week_dates()
        dates_in_current_week = get_dates_between(start_date, end_date)

        return dates_in_current_week
    
    def getWeekDays(date):
        date_object = datetime.strptime(date, "%Y-%m-%d")
        
        day_name = date_object.strftime("%A")
        return day_name  

    def isToday(date):
        date_object = datetime.strptime(date, '%Y-%m-%d')
        
        # Get today's date
        today = datetime.today().date()
        
        # Compare the dates
        if date_object.date() == today:
            return "today"
        elif date_object.date() < today:
            return "passed"
        else:
            return "upcoming"

    def getLastDate():
        database = Database()
        connection = database.connect()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('select * from last_date')
        query_result  = cursor.fetchall()

        cursor.close()
        connection.close()

        return query_result
    
    def setLastDate(date):
        connection = super().connect()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"update last_date set last_date ='{date}'" )
        query_result  = cursor.fetchall()

        connection.commit()
        cursor.close()
        connection.close()

        return query_result
    # def getStaff(self):
    #     connection = super().connect()
    #     cursor = connection.cursor(dictionary=True)
    #     cursor.execute('select * from staff')
    #     query_result  = cursor.fetchall()

    #     cursor.close()
    #     connection.close()

    #     return query_result
    
    # def insertStaff(self,staff, appointment):
    #     connection = super().connect()
    #     cursor = connection.cursor(dictionary=True)
    #     cursor.execute(f"INSERT INTO booked_staff (`staff_id`, `appointment_id`) VALUES ({staff}, {appointment})")

    #     connection.commit()
    #     cursor.close()
    #     connection.close()
    
    
    # def getStaffWhereAnd(self, rating, specialization):
    #     connection = super().connect()
    #     cursor = connection.cursor(dictionary=True)


    #     cursor.execute(f"SELECT * FROM staff WHERE rating = {rating} AND type = '{specialization}';")
    #     query_result  = cursor.fetchall()

    #     cursor.close()
    #     connection.close()

    #     return query_result  
    
    # def getStaffWhere(self,search, data):
    #     connection = super().connect()
    #     cursor = connection.cursor(dictionary=True)
    #     cursor.execute(f"select * from staff where {search} = '{data}' ")
    #     query_result  = cursor.fetchall()

    #     cursor.close()
    #     connection.close()

    #     return query_result  
    
    # # def insertUser(self,username, password):
    # #     connection = super().connect()
    # #     cursor = connection.cursor(dictionary=True)
    # #     cursor.execute(f"INSERT INTO users (`username`, `password`, `type`) VALUES ('{username}', '{password}', 'customer')")

    # #     connection.commit()
    # #     cursor.close()
    # #     connection.close()



