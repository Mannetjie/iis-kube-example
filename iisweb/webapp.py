from flask import Flask, render_template
from flask import jsonify
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/latlong')
def apiCall():
    r = requests.get(url='http://iss-api-service')
    #r = requests.get(url="http://api.open-notify.org/iss-now.json")
    responseJSON = r.json()
    response = jsonify(responseJSON);
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)