from flask import request, redirect, url_for, render_template
from app.models import *

class SignupController():

    def run(self):
        user = User()
        error = ''

        if request.method == 'POST':
            row = user.getUserWhere('username',  request.form.get('username'))
           
            if(not row):
                if(request.form.get('password') == request.form.get('confirm_password')):
                    user.insertUser(request.form.get('username'), request.form.get('password'))
                    row = {'username':request.form.get('username'), 'password':request.form.get('password')}   
                    Authentication.authenticate(row)
                    return redirect(url_for('routes.home'))
                else:
                    error = "Passwords Do Not Watch"
            else:
                error = "Username Has Been Taken"


        return render_template('signup.html', error = error)