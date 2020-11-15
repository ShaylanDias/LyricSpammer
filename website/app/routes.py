from app import app
import requests as rq
from flask import render_template, send_from_directory, request, jsonify
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
load_dotenv()

Timeout = rq.Timeout

limiter = Limiter(
    app,
    key_func=get_remote_address,
)



app.secret_key=os.getenv('secret_key').encode('utf-8')

app.config['DOWNLOAD_DIRECTORY'] = "./downloads/"

if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)

API_KEY = '3c36ae85a0c665724aa6ebca3a2715ef'
USER_AGENT = "lyricfinder"

@app.route('/')
@app.route('/index')
@limiter.exempt
def index():
    """Serves the frontend by rendering ."""
    return render_template('index.html')

@app.route('/download')
@limiter.exempt
def download():
    dir = app.config['DOWNLOAD_DIRECTORY']
    print(dir)
    print(os.path.exists(dir))
    return send_from_directory(dir, 'test.txt', as_attachment=True)


@app.route('/api/search')
@limiter.limit("1/second")
def forward_search_call():
    headers = {'user-agent': USER_AGENT}
    url = 'http://ws.audioscrobbler.com/2.0/'
    payload = dict(request.args) # Cast ImmutableMultiDict to Dict
    payload['api_key'] = API_KEY
    print('started request')
    print(payload)
    try:
        response = rq.get(url, headers=headers, params=payload, timeout=1)
    except Timeout as ex:
        print("Timeout Exception Raised: ", ex)
        raise InvalidUsage('Request Timed Out.', status_code=504)

    print('done with request')
    print(response.json())
    return response.json()

@app.route('/api/images')
@limiter.limit("4/second")
def forward_image_call():
    headers = {'user-agent': USER_AGENT}
    url = 'http://ws.audioscrobbler.com/2.0/'
    payload = dict(request.args) # Cast ImmutableMultiDict to Dict
    print(payload)
    payload['api_key'] = API_KEY
    try:
        response = rq.get(url, headers=headers, params=payload, timeout=1)
    except Timeout as ex:
        print("Timeout Exception Raised: ", ex)
        raise InvalidUsage('Request Timed Out.', status_code=504)
    return response.json()

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
