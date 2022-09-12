#import Flask class
from flask import request, make_response, redirect, render_template, session, redirect, url_for, flash
import unittest

from app import create_app
from app.forms import Login_Form

app =  create_app()

todos = ['Finish homework', 'Go to the gym', 'Go to the store']

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


#error handler for not page found
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

#route() decorator binds a function to a URL
@app.route('/')  
def index():
    user_ip = request.remote_addr #get the IP address of the user

    response = make_response(redirect('/hello')) #redirect to /hello
    session['user_ip'] = user_ip

    return response


@app.route('/hello', methods=['GET']) 
def hello():

    user_ip = session.get('user_ip')
    username = session.get('username')
    
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'username': username
    }

    return render_template('hello.html', **context) #render the template