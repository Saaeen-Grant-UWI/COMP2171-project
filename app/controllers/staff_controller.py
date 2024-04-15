from flask import request, redirect, url_for, render_template
from app.models import *

class StaffController():

    def run(self):
        if(Authentication.is_admin()):
            return render_template('barberpage.html')
        return redirect(url_for('routes.home'))
        