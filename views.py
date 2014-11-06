from __init__ import app
from flask import render_template

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
    render_template(check_property.html)

@app.route('/reference')
def reference():
    render_template('reference.html')