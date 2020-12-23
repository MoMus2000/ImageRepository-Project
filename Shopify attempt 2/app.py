from flask import Flask, session, request
from login import login_blueprint
import os
from signup import signup_blueprint
from upload import upload_blueprint
from image import image_blueprint
from image_manipulation import image_manipulation_blueprint

app = Flask(__name__)
"""
Api Service Written in flask using firebase. 
<br>
Author: Mustafa Muhammad
<br>
For : Shopify Technical Interview
<br>
Date : 21 December 2020
"""
app.secret_key = os.urandom(10)
app.register_blueprint(login_blueprint)
app.register_blueprint(signup_blueprint)
app.register_blueprint(upload_blueprint)
app.register_blueprint(image_blueprint)
app.register_blueprint(image_manipulation_blueprint)

@app.errorhandler(404)
def not_found(error):
	return 'Refer to api docs or source code for the correct path',404

if __name__ == "__main__":
	app.run(debug = True)



#Request parameter exception handling
#Generate Docs -- Done
#Update Read Me
#General Exception Handling