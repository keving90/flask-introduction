import hashlib
from flask import Flask, request, render_template, session, redirect
 
 # session object stores session information for a given user

app = Flask(__name__)

# A session will last for the specified amount of time. Default is 31 days.
# I'm using this to prevent an automatic login for a new session after an 
# initial login followed by a closed session.
app.permanent_session_lifetime = 0

USERNAME = 'admin'
PASSWORD = '81dc9bdb52d04dc20036dbd8313ed055' # password: 1234


@app.route('/')
def index():
    if 'username' not in session:
        return redirect('/login')
    return "You're logged in as {}".format(session['username'])


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_md5 = hashlib.md5(password.encode('utf-8')).hexdigest()
        if username == USERNAME and password_md5 == PASSWORD:
        # if username == USERNAME and password = PASSWORD:
            session['username'] = username
            return redirect('/')
        else:
            return "Invalid credentials"