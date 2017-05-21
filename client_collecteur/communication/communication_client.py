#!/usr/bin/python3
# coding: utf-8

from flask import Flask, jsonify, make_response
import json
from flask_httpauth import HTTPBasicAuth
from socket import *
from OpenSSL import SSL
import os
import subprocess

print('---------- ip local ----------')
args = ["hostname -I | awk '{ print $1 }'"]
proc = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE)
ip = proc.communicate()[0].decode("utf-8")

context = SSL.Context(SSL.SSLv23_METHOD)
cer = os.path.join(os.path.dirname(__file__), './/monitoring.com.crt')
key = os.path.join(os.path.dirname(__file__), './monitoring.com.key')

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
    return jsonify({'response': json.load(data_file)})


# Run
if __name__ == '__main__':
    context = (cer, key)
    app.run(
        host=ip,
        port=5000,
        ssl_context=context,
        threaded=True
    )
