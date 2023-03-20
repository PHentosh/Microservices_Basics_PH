from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
      dat = str(request.data)[2:-1]
      logging = requests.post('http://localhost:8081', data=dat).content
      return logging
    else:
      logging = requests.get('http://localhost:8081').content
      mess = requests.get('http://localhost:8082').content
      return str(mess)[2:-1] + ": " + str(logging)[2:-1]
       
if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)