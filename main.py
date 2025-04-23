from fetchCookies import fetch_token_and_cookies
from flask import Flask, jsonify, request
from flask_cors import CORS
from makeRequests import getBaseData, getPatternPaths, getVehicles
import json


def startup():
    #startup
    print("Starting...")
    #fetch cookies
    cookies = fetch_token_and_cookies()

    #save to file
    with open('cookies.json', 'w') as f:
        import json
        json.dump(cookies, f)

startup()