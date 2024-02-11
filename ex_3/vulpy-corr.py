import os
from pathlib import Path

from flask import Flask, g, redirect, request

import libsession
from mod_api import mod_api
from mod_csp import mod_csp
from mod_hello import mod_hello
from mod_mfa import mod_mfa
from mod_posts import mod_posts
from mod_user import mod_user

app = Flask('vulpy')

# Use environment variable for debug mode
app.debug = os.environ.get('FLASK_DEBUG', False)  # Defaults to False for security

app.config['SECRET_KEY'] = '!9h1j2k3l$4p5q6r7s%8t9u0v@1w2x3y4z5Z6X7C8V9B0N%M'  # Use a strong, unique secret key

app.register_blueprint(mod_hello, url_prefix='/hello')
app.register_blueprint(mod_user, url_prefix='/user')
app.register_blueprint(mod_posts, url_prefix='/posts')
app.register_blueprint(mod_mfa, url_prefix='/mfa')
app.register_blueprint(mod_csp, url_prefix='/csp')
app.register_blueprint(mod_api, url_prefix='/api')

csp_file = Path('csp.txt')
csp = ''

if csp_file.is_file():
    with csp_file.open() as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            line = line.replace('\n', '')
            if line:
                csp += line
if csp:
    print('CSP:', csp)

@app.route('/')
def do_home():
    return redirect('/posts')

@app.before_request
def before_request():
    g.session = libsession.load(request)

@app.after_request
def add_csp_headers(response):
    if csp:
        response.headers['Content-Security-Policy'] = csp
    return response

if __name__ == '__main__':
    # Run the app in production mode with debug disabled by default
    app.run(host='127.0.1.1', port=5000, extra_files='csp.txt')
