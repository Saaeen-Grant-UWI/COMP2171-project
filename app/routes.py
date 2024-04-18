from flask import Blueprint, render_template
from app.controllers import *

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    controller = HomeController()
    return controller.run()

@routes.route('/login', methods=["POST", "GET"])
def login():
    controller = LoginController()
    return controller.run()

@routes.route('/logout')
def logout():
    controller = LogoutController()
    return controller.run()

@routes.route('/signup', methods=["POST", "GET"])
def signup():
    controller = SignupController()
    return controller.run()

@routes.route('/dashboard', methods=["POST", "GET"])
def dashboard():
    controller = DashboardController()
    return controller.run()

@routes.route('/appointment', methods=["POST", "GET"])
def appointment():
    controller = AppointmentController()
    return controller.run()


@routes.route('/filter', methods=["POST", "GET"])
def filter():
    controller = FilterController()
    return controller.run()

@routes.route('/staff', methods=["POST", "GET"])
def staff():
    controller = StaffController()
    return controller.run()


@routes.route('/reschedule/<appointment_id>/', methods=["POST", "GET"])
def reschedule(appointment_id):
    controller = AppointmentController()
    return controller.run(appointment_id)

@routes.route('/appointment_update/<appointment_id>/', methods=["POST", "GET"])
def appointment_update(appointment_id):
    controller = AppointmentController()
    return controller.appointmentUpdate(appointment_id)

@routes.route('/appointment_cancel/<appointment_id>/', methods=["POST", "GET"])
def appointment_cancel(appointment_id):
    controller = DashboardController()
    return controller.cancelAppointment(appointment_id)

@routes.route('/appointment_activate/<appointment_id>/', methods=["POST", "GET"])
def appointment_activate(appointment_id):
    controller = DashboardController()
    return controller.activateAppointment(appointment_id)

@routes.route('/appointment_delete/<appointment_id>/', methods=["POST", "GET"])
def appointment_delete(appointment_id):
    controller = DashboardController()
    return controller.deleteAppointment(appointment_id)
