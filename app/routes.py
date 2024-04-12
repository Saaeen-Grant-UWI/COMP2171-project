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