from flask import Flask, url_for, redirect, render_template
from main import send_login

import jinja2

app = Flask(__name__)
title = "Jinja and flask"
info = ["My first site", "My info"]

@app.route('/redirect_login/')
def redirect_login():
    return redirect(url_for(send_login))

@app.route('/')
def main_page():
    return render_template('base.html', info=info, title=title)


app.run(port=34000)