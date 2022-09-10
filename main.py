#import Flask class
from flask import Flask, request, make_response, redirect, render_template

#instantiate Flask class
app = Flask(__name__)  #__name__ is the name of the current python module

app.config['Secret_Key'] = 'ThisIsSecret'

todos = ['Finish homework', 'Go to the gym', 'Go to the store']

#error handler for not page found
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

#route() decorator binds a function to a URL
@app.route('/')  
def index():
    user_ip = request.remote_addr #get the IP address of the user

    response = make_response(redirect('/hello')) #redirect to /hello
    response.set_cookie('user_ip', user_ip) #set a cookie

    return response


@app.route('/hello') 
def hello():
    user_ip = request.cookies.get('user_ip') #get the cookie
    context = {
        'user_ip': user_ip,
        'todos': todos
    }

    return render_template('hello.html', **context) #render the template