#!/usr/bin/env python3

import json
import random

from flask import Flask, redirect, request

app = Flask(__name__)
db = {}
URL_BASE = 'http://localhost:5000/'


def save_short_url(original_url):
    short_url = ''.join(random.choice('0123456789abcdef') for i in range(10))
    db[short_url] = original_url
    return short_url


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/create', methods=['POST'])
def create_short_url():
    original_url = request.get_json().get('url')
    short_url = save_short_url(original_url)
    return URL_BASE + 'tiny/' + short_url


@app.route('/tiny')
def list_short_urls():
    return json.dumps(db)


@app.route("/tiny/<string:short_url>")
def get_short_url(short_url):
    return redirect(db.get(short_url), code=302)


@app.route("/tiny_debug/<string:short_url>")
def get_short_url_debug(short_url):
    return 'Short URL: {}'.format(short_url)


if __name__ == "__main__":
    app.run()
