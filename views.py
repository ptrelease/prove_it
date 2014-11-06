import random
import string
from __init__ import app
from flask import render_template, Response, request
from twilio.rest import TwilioRestClient
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
    code = code_generator()
    qr_generator.generate_qr_code(code)
    return render_template('reference.html', code=code)

@app.route('/login')
def login():
    return render_template('choose_to_prove.html')


@app.route('/sendsms', methods=['POST'])
def send_sms():
    # put your own credentials in a config.py
    ACCOUNT_SID = app.config['ACCOUNT_SID']
    AUTH_TOKEN = app.config['AUTH_TOKEN']
    ref_code = request.form.get('ref_code')
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    client.messages.create(
        to=app.config['TO_TEST_NUMBER'],
        from_=app.config['FROM_TEST_NUMBER'],
        body="your reference is " + ref_code
        )

    return Response("message sent", status=200)

@app.route('/base')
def base():
    return render_template('global/base.html')

def code_generator(size=8, chars=(string.ascii_uppercase + string.digits)):
    return ''.join(random.choice(chars) for _ in range(size))
