from flask import Flask
from flask import jsonify
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello():
    #send request to outside api for ISS position
    r = requests.get(url="http://api.open-notify.org/iss-now.json")
    #get JSON object from request
    issJson = r.json()
    #isolate Location object
    issLocation = issJson["iss_position"]
    #if request was a success transform into new object that we will send back
    if issJson["message"] == "success":
        retObj = {
            "type": "FeatureCollection",
            "error": "none",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [issLocation["longitude"],issLocation["latitude"]]
                    },
                    "properties": {
                        "title": "Mapbox",
                        "description": "International Space Station"
                    }
                }
            ]
        }
    else:
        retObj = {
            "error": "error"
        }
    #create the response that will be sent back
    response = jsonify(retObj);
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)