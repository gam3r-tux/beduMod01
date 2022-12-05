import time

import redis
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    resp = Response('{ "body" : "Service open with python version ==> ' + sys.version + ' <== "}')
    resp.headers['Content-Type'] = 'application/json'
    return resp
