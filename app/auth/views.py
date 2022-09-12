import imp
from multiprocessing import context
from . import auth
from app.forms import Login_Form
from flask import render_template

@auth.route('/login')
def login():
    context = {
        'login_form': Login_Form()
    }
    return render_template('login.html', **context)