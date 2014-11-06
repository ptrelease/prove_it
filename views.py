from __init__ import app
from flask import render_template
from qr import qr_generator

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/choose')
def choose():
    return render_template("choose_to_prove.html")

@app.route('/searchforproperty')
def searchforproperty():
    return render_template('search_for_property.html')

@app.route('/checkproperty')
def check_property():
    return render_template('check_property.html')

@app.route('/reference')
def reference():
    code = "SHF3HFH7"
    qr_generator.generate_qr_code(code)
    return render_template('reference.html')
    render_template('reference.html')


@app.route('/login')
def login():
    return render_template('choose_to_prove.html')

@app.route('/base')
def base():
    return render_template('global/base.html')
