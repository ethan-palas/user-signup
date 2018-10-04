from flask import Flask, request, redirect, render_template
import os


app = Flask(__name__)
app.config['DEBUG'] = True 


@app.route("/", methods = ['GET', 'POST'])
def index():
    username = request.args.get('username')
    return render_template('user_form.html')

@app.route('/valid-input', methods = ['POST'])
def valid_input():

    if request.method == 'POST':

        username = request.form['user-name']
        password = request.form['password']
        verify_pw = request.form['verify-pw']
        email = request.form['email']

        username_error = ''
        password_error = ''
        verify_pw_error = ''
        email_error = ''



    if not username:
        username_error = 'You must create a username'
    elif (len(username) < 3) or (len(username) > 20):
        username_error = 'Username must be greater than 3 characters but less than 20'
    elif " " in username:
        username_error = "Username must not have spaces"
    else:
        pass


    if not password:
        password_error = 'You must create a password'
    elif (len(password) < 3) or (len(password) > 20):
            password_error = 'Password must be greater than 3 characters but less than 20'
    elif " " in password:
            password_error = "Password must not have spaces"
    else:
        pass

    if not verify_pw:
        verify_pw_error = 'You must verify a password'
    elif (len(password) < 3) or (len(password) > 20):
            password_error = 'Password must be greater than 3 characters but less than 20'
    elif " " in password:
            password_error = "Password must not have spaces"
    else:
        pass


    if verify_pw != password:
        verify_pw_error = 'Passwords must match'
        password_error = 'Passwords must match'
    else:
        pass


    if email != "":

        if not "@" in email:
            email_error = 'Not a valid email'
        elif not "." in email:
            email_error = 'Not a valid email'
        elif " " in email:
            email_error = 'Not a valid email'
        elif (len(email) < 3) or (len(email) > 20):
            email_error = 'Not a valid email'
        else:
            pass

    if not username_error and not password_error and not verify_pw_error and not email_error:
        return render_template('user_welcome.html', username=username)


    return render_template('user_form.html', username_error=username_error, password_error=password_error, verify_pw_error=verify_pw_error, email_error=email_error)

app.run()
