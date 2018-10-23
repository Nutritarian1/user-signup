from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('form.html') 

@app.route('/', methods=['POST'])
def validate_form():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    user_error = ''
    pass_error = ''
    verify_error = ''
    email_error = ''

    if len(username) not in range(3,21) or ' ' in username:
        user_error = "That's not a valid username"
        username=''
    
    if len(password) not in range(3,21) or ' ' in password:
        pass_error = "That's not a valid password"
        password=''
    
    if verify != password:
        verify_error = "Passwords don't match."
        verify=''
    
    if email != '':
        dot1=email.count('.') == 1
        at1=email.count('@') == 1
        space0=email.count(' ') == 0
        if not (dot1 and at1 and space0) or len(email) not in range(3,21):
            email_error = "That's not a valid email."
            email=''
    
    if not user_error and not pass_error and not verify_error and not email_error:
        return redirect('/welcome?username=' + username) 
    else:
        return render_template('form.html', user_error=user_error,
            pass_error=pass_error,
            verify_error=verify_error,
            email_error=email_error,
            username=username,
            password='',
            verify='',
            email=email)

@app.route('/welcome')
def welcome_msg():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()