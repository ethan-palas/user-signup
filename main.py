from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

template_dir = os.path.join(os.path.dirname(__file__),
    'templates')

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir))


@app.route('/user-signup')
def display_user_signup():
    user_template= jinja_env.get_template('user_form.html')
    return user_template.render(username_error='')

app.run()

