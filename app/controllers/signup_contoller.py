from flask import request, redirect, url_for, render_template
from app.models import *

class SignupController():

    def run(self):
        user = User()
        test = {}

        if request.method == 'POST':
            row = user.getUserWhere('username',  request.form.get('username'))
           
            if(not row):
                if(request.form.get('password') == request.form.get('confirm_password')):
                    user.insertUser(request.form.get('username'), request.form.get('password'))
                    row = {'username':request.form.get('username'), 'password':request.form.get('password')}   
                    Authentication.authenticate(row)
                    return redirect(url_for('routes.home'))


        return render_template('signup.html', data = test)