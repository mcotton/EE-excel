from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from functools import wraps

from EagleEye import *


een_sessions = {}
 
app = Flask(__name__)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return render_template('login.html')
        return f(*args, **kwargs)
    return decorated_function


 
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return f"Hello {session['name']}!  <a href=\"/logout\">Logout</a>"
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    if 'id' in session:
        if session['id'] in een_sessions:
            pass
        else:
            een = EagleEye()
            een_sessions[session['id']] = een 
    else:
        session['id'] = os.urandom(16)
        een = EagleEye()
        een_sessions[session['id']] = een

    
    if een.login(username=request.form['username'], password=request.form['password']):
        session['logged_in'] = True
        session['name'] = f"{een.user['first_name']} {een.user['last_name']}"
        
        

    else:
        flash('wrong password!')
    
    return home()
 
@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['name'] = ''
    del een_sessions[session['id']]
    session['id'] = None
    return home()
 

@app.route("/devices")
@login_required
def list_devices():
    een = een_sessions[session['id']]
    return render_template('devices.html', cameras=een.cameras)

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
