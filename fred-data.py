# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, request

import sys

import math
import codecs
import argparse
import re
import requests
import json


TIMEOUT = 10


app = Flask(__name__)

@app.route('/', methods=['GET'])
def test_connectivity():

    return "success"

@app.route('/fred/series/search', methods=['GET'])
def get_fred_series_by_sector():

    search_text = request.args.get('text', '')
    limit  = request.args.get('limit', 1000)
    offset = request.args.get('offset', 0)

    payload = {
        "search_text": search_text,
        "api_key": '686499b1e93cfa261ddef9faa553f4b9',
        "file_type": 'json',
        "limit": limit,
        "offset": offset
    }

    url = 'https://api.stlouisfed.org/fred/series/search'

    response = requests.get(url, params=payload, verify=False)

    return response.text


@app.route('/fred/series/<string:id>', methods=['GET'])
def get_fred_series(id):

    payload = {
        "series_id": id,
        "api_key": '686499b1e93cfa261ddef9faa553f4b9',
        "file_type": 'json'
    }
    url = 'https://api.stlouisfed.org/fred/series/observations'
    response = requests.get(url, params=payload, verify=False)

    return response.text

if __name__ == '__main__':

    app.run(debug=True, host="0.0.0.0", port=5001)
