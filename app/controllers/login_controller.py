from flask import request, redirect, url_for, render_template
from app.models import *

class LoginController():

    def run(self):
        user = User()
        if request.method == 'POST':
            row = user.getUserWhere('username',  request.form.get('username'))[0]
            
            if(row):
                if(request.form.get('password') == row['password'] ):
                    Authentication.authenticate(row)
                    return redirect(url_for('routes.home'))
            
        return render_template('login.html', Authentication = Authentication)