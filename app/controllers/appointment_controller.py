from flask import request, redirect, url_for, render_template
from app.models import *
from datetime import datetime

class AppointmentController():

    def run(self, id = None):
        appointment = Appointment()
        service = Service()
        staff = Staff()
        appointments = sorted(appointment.getCustomerAppointment(int(Authentication.get_user()['id'])), key=lambda x: x['id'], reverse=True)[0]
        services = []
        times = ['9:00 AM', '10:00 AM', '11:00 AM', '12:00 PM', '1:00 PM', '2:00 PM', '3:00 PM', '4:00 PM', '5:00 PM', '6:00 PM']
        
        for item in service.getServices():
            item_temp = item['service'].lower()
            item['service_tag'] = item_temp.replace(" ", "_")
            services.append(item)


        
        time_date = {}

        for entry in appointment.getDateTime():
            date = entry['date']
            time = entry['time']
            status =  entry['status']
            if status == 'active':
                if date in time_date:
                    time_date[date].append(time)
                else:
                    time_date[date] = [time]

        
        # Get form data
        error = ''
        if request.method == 'POST':

            appointment_data = {
                'appointment_date': request.form.get('appointmentDate'),
                'appointment_time': request.form.get('appointmentTime'),
                'payment_method': request.form.get('payment'),
                'price': request.form.get('price')
            }
            if(appointment.checkAppointments(appointment_data['appointment_date'], appointment_data['appointment_time'])):
                error = datetime.strptime(appointment_data['appointment_date'], "%Y-%m-%d").strftime("%A, %B %d, %Y") +" "+appointment_data['appointment_time']+" "+'is Already Booked'
            else:
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
    
        if(request.url_rule.rule == '/appointment'):
            return render_template('barberselection.html', Authentication = Authentication, error = error, appointments = appointments, services = services, date = Calender, times = times, time_date = time_date)
        

        return render_template('reschedule.html', Authentication = Authentication, appointments = appointments, services = services, date = Calender, times = times, time_date = time_date, appointment_user = appointment.getAppointmentById(id)[0])
    
    def appointmentUpdate(self, appointment_id):
        if request.method == 'POST':
            if(Appointment().checkAppointments(request.form['appointmentDate'], request.form['appointmentTime'])):
                error = datetime.strptime(request.form['appointmentDate'], "%Y-%m-%d").strftime("%A, %B %d, %Y") +" "+request.form['appointmentTime']+" "+'is Already Booked'
                return render_template('reschedule_warning.html', error=error, appointment_id=appointment_id)
            Appointment().updateAppointment(request.form['appointmentDate'], request.form['appointmentTime'], request.form['payment'], appointment_id)
            return redirect(url_for('routes.dashboard'))