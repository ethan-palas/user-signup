from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

user_form = """
    <style>
        .error {{ color: red;}}
    </style>
    <h1>User Signup</h1>
    <form method='POST'>
        <label>Username
            <input name="username" type="text" value='{username}' />
        </label>
        <p class="error">{username_error}</p>
        <label>Password
            <input name="password" type="text" value='{password}' />
        </label>
        <p class="error">{password_error}</p>
        <label>Confirm Password
            <input name="confirm_password" type="text" value={confirm_password} />
        </label>
        <p class="error">{confirm_error}</p>
        <label>Email
            <input name="email" type="text" value={email} />
        </label>
        <p class="error">{email_error}</p>
        <input type="submit" value="Convert" />
    </form>
"""

@app.route('/user-signup')
def display_user_signup():
    return user_form.format(username='', username_error='',
    password='', password_error='',
    confirm_password='', confirm_error='',
    email='',email_error='',
)

app.run()