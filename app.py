#flask server that serves the endpoints in makeRequests.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from makeRequests import getBaseData, getPatternPaths, getVehicles
import json

app = Flask(__name__)
CORS(app)



def load_cookies():
    with open('cookies.json', 'r') as f:
        cookies = json.load(f)
        return cookies



@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/get_base_data', methods=['GET'])
def base_data():
    # Use cookies to call getBaseData
    print(cookies)
    response = getBaseData(
        cookies['TSSESSIONID'],
        cookies['.MyRide.RequestVerificationToken'],
        cookies['RequestVerificationToken']
    )
    return jsonify(response)

@app.route('/get_pattern_paths', methods=['POST'])
def pattern_paths():
    # Get routeKeys from the request body
    routeKeys = request.json.get('routeKeys[]', [])
    print(routeKeys)
    # Use cookies to call getPatternPaths
    response = getPatternPaths(
        cookies['TSSESSIONID'],
        cookies['.MyRide.RequestVerificationToken'],
        cookies['RequestVerificationToken'],
        routeKeys
    )
    return jsonify(response)

@app.route('/get_vehicles', methods=['POST'])
def vehicles():
    # Get routeKeys from the request body
    routeKeys = request.json.get('routeKeys[]', [])
    # Use cookies to call getVehicles
    response = getVehicles(
        cookies['TSSESSIONID'],
        cookies['.MyRide.RequestVerificationToken'],
        cookies['RequestVerificationToken'],
        routeKeys
    )
    return jsonify(response)

if __name__ == '__main__':
    cookies = load_cookies()
    app.run(debug=True)

