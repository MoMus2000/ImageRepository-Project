from flask import Flask, session, request
from login import login_blueprint
import os
from signup import signup_blueprint
from upload import upload_blueprint
from image import image_blueprint
from image_manipulation import image_manipulation_blueprint


"""
Api Service Written in flask using firebase for authentication and database. 
Author: Mustafa Muhammad
For : Shopify Technical Interview
Date : 21 December 2020
"""




app = Flask(__name__)
app.secret_key = os.urandom(10)
app.register_blueprint(login_blueprint)
app.register_blueprint(signup_blueprint)
app.register_blueprint(upload_blueprint)
app.register_blueprint(image_blueprint)
app.register_blueprint(image_manipulation_blueprint)

app.run(debug = True)



#Request parameter exception handling
#Generate Docs -- Done
#Update Read Me
#General Exception Handling