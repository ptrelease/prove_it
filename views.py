from __init__ import app
from flask import render_template, Response
from twilio.rest import TwilioRestClient

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
    return render_template('reference.html')
    render_template('reference.html')

@app.route('/login')
def login():
    return render_template('choose_to_prove.html')

@app.route('/sendsms')
def send_sms():
    # put your own credentials in a config.py
    ACCOUNT_SID = app.config['ACCOUNT_SID']
    AUTH_TOKEN = app.config['AUTH_TOKEN']

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    client.messages.create(
        to=app.config['TO_TEST_NUMBER'],
        from_=app.config['FROM_TEST_NUMBER'],
        body="a reference",
        )

    return Response("message sent", status=200)
                                                                                         --data-urlencode 'Body=Hello paul, welcome to Twilio!'