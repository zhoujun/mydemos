# -*- coding: UTF-8 -*-

from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    'finger': 'hellofinger',
    'scott': 'tiger'
}

@auth.get_password
def get_password(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/')
@auth.login_required
def index():
    return 'Hello, %s!' % auth.username()

if __name__ == '__main__':
    app.run()
