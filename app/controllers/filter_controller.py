from flask import request, redirect, url_for, render_template
from app.models import *

class FilterController():

    def run(self):
        data = []
        staff = Staff()
        if request.method == 'POST':
            temp =  {'specialization':request.form.get("specialization"),'rating':request.form.get("rating")}

            if temp['specialization'] == '*' and temp['rating'] == '*':
                data = staff.getStaff()
            elif temp['specialization'] != '*' and temp['rating'] == '*':
                data = staff.getStaffWhere('type', temp['specialization'])
            elif temp['specialization'] == '*' and temp['rating'] != '*':
                data = staff.getStaffWhere('rating', temp['rating'])
            else:
                data = staff.getStaffWhereAnd(temp['rating'], temp['specialization'])
            

        return render_template('filter.html', Authentication = Authentication, data = data)