from flask import request, redirect, url_for, render_template
from app.models import *

class HomeController():

    def run(self):
        return render_template('index.html', Authentication = Authentication)