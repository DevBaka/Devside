# -*- coding: utf-8 -*-
from flask import Flask, logging
from flask import url_for
import os
import sys
# import flask.ext.login as flask_login
import flask_login




app = Flask(__name__)
wsgi_app = app.wsgi_app
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
app.secret_key = os.urandom(24)
from routes import *


if __name__ == '__main__':
    HOST = os.environ.get("SERVER_HOST", "localhost")
    try:
        PORT = int(os.environ.get("SERVER_PORT", "4444"))
    except ValueError:
        PORT = 4444
    app.run(HOST, PORT, debug=True)

if sys.version_info.major < 3:
    reload(sys)
sys.setdefaultencoding('utf8')