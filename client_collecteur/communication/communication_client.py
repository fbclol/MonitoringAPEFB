#!/usr/bin/python3
# coding: utf-8

from flask import Flask, render_template, request, jsonify
import json
import stripe
import smtplib
import requests
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return "Hello test !"

@app.route('/api/monitoring')
def summary():
    data_file = open('../stockage_collection/collecteur_final.json')
    data = json.load(data_file)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

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





