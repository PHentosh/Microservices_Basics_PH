from flask import Flask, request
import requests
import json
import uuid


messages = {}
app = Flask(__name__)

@app.get('/')
def login_get():
    global messages
    return str(messages)

@app.post('/')
def login_post():
    global messages
    mess = request.data
    u = uuid.uuid4().hex
    messages[u] = str(mess)[2:-1]
    print(mess)
    return "message registered"


if __name__ == '__main__':
    app.run(host="localhost", port=8081, debug=True)