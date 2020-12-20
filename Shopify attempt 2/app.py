from flask import Flask, session, request
from login import login_blueprint
import os
from signup import signup_blueprint
from upload import upload_blueprint

app = Flask(__name__)
app.secret_key = os.urandom(10)
app.register_blueprint(login_blueprint)
app.register_blueprint(signup_blueprint)
app.register_blueprint(upload_blueprint)

app.run(debug = True)