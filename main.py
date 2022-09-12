#import Flask class
from flask import Flask, request, make_response, redirect, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest

#instantiate Flask class
app = Flask(__name__)  #__name__ is the name of the current python module

app.config['SECRET_KEY'] = 'SUPER SECRETO'

todos = ['Finish homework', 'Go to the gym', 'Go to the store']


class Login_Form(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Send')


@app.cli.command()
def test():
    test = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(test)

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


@app.route('/hello', methods=['GET', 'POST']) 
def hello():

    user_ip = session.get('user_ip')
    login_form = Login_Form()
    username = session.get('username')
    
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
        'username': username
    }

    if request.method == 'POST': #if the form is submitted and validated
        username = login_form.username.data
        session['username'] = username
        flash('Nombre de usario registrado con éxito!')

        return redirect(url_for('index'))

    return render_template('hello.html', **context) #render the template