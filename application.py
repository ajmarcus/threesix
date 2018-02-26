#! /usr/bin/env python

from typing import NamedTuple
from flask import Flask
app = Flask(__name__)

class User(NamedTuple):
    name: str

@app.route('/')
def hello_world():
    return 'Hello python!'

@app.route('/<name>')
def hello(name):
    user = User(name)
    return f'Hello {user.name}'

if __name__ == '__main__':
    app.run(debug=True)
