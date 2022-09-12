from . import auth
from app.forms import Login_Form
from flask import render_template, redirect, url_for, request, session, flash

@auth.route('/login', methods=['GET', 'POST'])
def login():

    login_form = Login_Form()

    context = {
        'login_form': login_form
    }

    if request.method == 'POST': #if the form is submitted and validated

        username = login_form.username.data
        session['username'] = username
        flash('Nombre de usario registrado con éxito!')

        return redirect(url_for('index'))

    return render_template('login.html', **context) #render the template