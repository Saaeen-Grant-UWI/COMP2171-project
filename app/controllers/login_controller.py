from flask import request, redirect, url_for, render_template
from app.models import *

class LoginController():

    def run(self):
        user = User()
        error = ''
        if request.method == 'POST':
            row = user.getUserWhere('username',  request.form.get('username'))
            
            if(row):
                row = row[0]
                if(request.form.get('password') == row['password'] ):
                    Authentication.authenticate(row)
                    return redirect(url_for('routes.home'))
                else:
                    error = "Wrong Password"
            else:
                error = "User Not Found"

                
            
        return render_template('login.html', Authentication = Authentication, error = error)