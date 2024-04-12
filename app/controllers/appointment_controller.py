from flask import request, redirect, url_for, render_template
from app.models import *

class AppointmentController():

    def run(self):
        appointment = Appointment()
        service = Service()
        staff = Staff()
        appointments = Appointment().getCustomerAppointment(int(Authentication.get_user()['id']))
        
        # Get form data
        if request.method == 'POST':

            appointment_data = {
                'appointment_date': request.form.get('appointmentDate'),
                'appointment_time': request.form.get('appointmentTime'),
                'payment_method': request.form.get('payment'),
                'price': request.form.get('price')
            }
            appointment.insertAppointment(appointment_data['appointment_date'], appointment_data['appointment_time'], appointment_data['payment_method'], appointment_data['price'], Authentication.get_user()['id'])

            service_data = {'selected_services': request.form.getlist('service')}
            for service_item in service_data['selected_services']:
                service.insertService(int(service_item), appointment.getLastAppointmentId())

            stylist_data = {
                'preferred_barber': request.form.get('barbers'),
                'preferred_stylist': request.form.get('stylist')
            }
            staff.insertStaff(int(stylist_data['preferred_barber']), appointment.getLastAppointmentId())
            staff.insertStaff(int(stylist_data['preferred_stylist']), appointment.getLastAppointmentId())
            return redirect(url_for('routes.dashboard'))

            

        return render_template('barberselection.html', Authentication = Authentication, appointments = appointments)