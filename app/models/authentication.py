from flask import session

class Authentication:

    @staticmethod
    def authenticate(row):
        if(type(row) is dict):
            session['user'] = row

    @staticmethod
    def logged_in():
        if('user' in session):
             return True 
        return False
    
    @staticmethod
    def logout():
        if('user' in session):
             session.pop('user',None)
        return False
    
    @staticmethod
    def is_admin():
        if('user' in session):
            return session['user']['type'] == 'admin'
        return True
    
    @staticmethod
    def get_type():
        if('user' in session):
            return session['user']['type']
        return False
    
    @staticmethod
    def get_user():
        if('user' in session):
            return session['user']
        return False