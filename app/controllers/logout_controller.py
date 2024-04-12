from flask import request, redirect, url_for, render_template
from app.models import *

class LogoutController():

    def run(self):
        Authentication.logout()
        return redirect(url_for('routes.home'))