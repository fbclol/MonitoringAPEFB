#!/usr/bin/python3
# coding: utf-8

from flask import Flask, render_template, request, jsonify,make_response
import json
#import stripe
#import smtplib
#import requests
from flask_httpauth import HTTPBasicAuth


auth = HTTPBasicAuth()
app = Flask(__name__)
app.debug = True




@auth.get_password
def get_password(username):
    if username == 'monitoring':
        return 'p7tH0n@#!'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'response': 'Unauthorized access'}), 403)


@app.route('/')
def index():
    return "Hello test !"

@app.route('/api/monitoring', methods=['GET'])
@auth.login_required
def summary():
    data_file = open('../stockage_collection/collecteur_final.json')
    #data = json.load(data_file)
    #response = app.response_class(
    #   response=json.dumps(data),
    #    status=200,
    #    mimetype='application/json'
    #)
    # return response
    return jsonify({'response': json.load(data_file)})


# Run
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(
        host = "172.17.0.2",
        port = 5000
    )



#@app.route('/')
#def index():
    # Render template
#    return render_template('index.html')





