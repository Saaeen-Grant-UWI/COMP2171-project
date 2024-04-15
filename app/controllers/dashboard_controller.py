from flask import request, redirect, url_for, render_template
from datetime import datetime, timedelta
from app.models import *

class DashboardController():

    def run(self):
        if(Authentication.is_admin()):
            appointments = []
            user = User()
            for item in Appointment().getAppointments():
                item_temp =  datetime.strptime(item['date'], "%Y-%m-%d")
                item['date'] = item_temp.strftime("%A, %B %d, %Y")
                item['customer_id'] = user.getUserById(item['customer_id'])[0]['username']
                appointments.append(item)
        else:
            appointments =sorted(Appointment().getCustomerAppointment(int(Authentication.get_user()['id'])), key=lambda x: x['id'], reverse=True)
            
            if(appointments):
                appointments = appointments[0]
                appointments['date'] = datetime.strptime(appointments['date'], "%Y-%m-%d").strftime("%A, %B %d, %Y")
            else:
                appointments = []

        
        return render_template('admin.html', Authentication = Authentication, appointments = appointments, date = Calender)
    
    def cancelAppointment(self, appointment_id):
        if(Authentication.logged_in()):
            Appointment().updateAppointmentSatus('cancelled', appointment_id)
            return redirect(url_for('routes.dashboard'))
        return redirect(url_for('routes.dashboard'))


    def activateAppointment(self, appointment_id):
        if(Authentication.is_admin()):
            Appointment().updateAppointmentSatus('active', appointment_id)
            return redirect(url_for('routes.dashboard'))
        return redirect(url_for('routes.dashboard'))
    
    def deleteAppointment(self, appointment_id):
        Appointment().deleteAppointment(appointment_id)
        return redirect(url_for('routes.dashboard'))