from flask import request, redirect, url_for, render_template
from app.models import *

class DashboardController():

    def run(self):
        if(Authentication.is_admin()):
            appointments = Appointment().getAppointments()
        else:
            appointments = Appointment().getCustomerAppointment(int(Authentication.get_user()['id']))
            
            if(appointments):
                appointments = [appointments[0]]
            else:
                appointments = []





        return render_template('admin.html', Authentication = Authentication, appointments = appointments)