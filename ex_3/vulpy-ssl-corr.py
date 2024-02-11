import os
from flask import Flask, g, redirect, request

from mod_hello import mod_hello
from mod_user import mod_user
from mod_posts import mod_posts
from mod_mfa import mod_mfa

import libsession

app = Flask('vulpy')

# Use environment variable for debug mode (defaults to False for security)
app.debug = os.environ.get('FLASK_DEBUG', False)

app.config['SECRET_KEY'] = '!9h1j2k3l$4p5q6r7s%8t9u0v@1w2x3y4z5Z6X7C8V9B0N%M'  # Use a strong, unique secret key

app.register_blueprint(mod_hello, url_prefix='/hello')
app.register_blueprint(mod_user, url_prefix='/user')
app.register_blueprint(mod_posts, url_prefix='/posts')
app.register_blueprint(mod_mfa, url_prefix='/mfa')

@app.route('/')
def do_home():
    return redirect('/posts')

@app.before_request
def before_request():
    g.session = libsession.load(request)

if __name__ == '__main__':
    # Run the app in production mode with debug disabled by default
    app.run(debug=False,host='127.0.1.1', port=5000, ssl_context=('/tmp/acme.cert', '/tmp/acme.key'))