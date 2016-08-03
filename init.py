# -*- coding: utf-8 -*-
from flask import Flask, logging
from flask import url_for
import os
import sys
from werkzeug.utils import secure_filename
from werkzeug import SharedDataMiddleware
# import flask.ext.login as flask_login
#import flask_login

UPLOAD_FOLDER = 'Uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', ".rar", ".7z", ".exe"])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
wsgi_app = app.wsgi_app
#login_manager = flask_login.LoginManager()
#login_manager.init_app(app)
app.add_url_rule('/uploads/<filename>', 'uploaded_file',build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/uploads':  app.config['UPLOAD_FOLDER']
})

app.secret_key = os.urandom(24)
from routes import * 


if __name__ == '__main__':
    HOST = os.environ.get("SERVER_HOST", "192.168.2.100")
    try:
        PORT = int(os.environ.get("SERVER_PORT", "4444"))
    except ValueError:
        PORT = 4444
    app.run(HOST, PORT, debug=True)

if sys.version_info.major < 3:
    reload(sys)
sys.setdefaultencoding('utf8')