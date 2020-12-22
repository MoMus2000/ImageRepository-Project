from flask import Flask, request, session, Blueprint
import pyrebase
import uuid
from constant import config


upload_blueprint = Blueprint('upload_blueprint', __name__)





#Add an image to storage and put the link into the data base according to the user
@upload_blueprint.route("/upload", methods = ["POST"])
def uploadSingleImage():
	"""
	Method: Upload an image to firebase using user account
	<br>
	Request: POST
	<br>
	Use: Upload Image to Firebase Storage Bucket and at the same time set the link with the user in the database.
	"""
	if(session.get('id') == None):
		return 'Please Login First', 401
	firebase = pyrebase.initialize_app(config)
	storage = firebase.storage()
	path = request.json['path']
	text = request.json['text']
	name = request.json['name']
	_id = str(uuid.uuid4())
	pic = storage.child(_id).put(path) #Getting pic url
	url = storage.child(_id).get_url(session['user'])
	db = firebase.database()
	data = {
		"title": name,
		"Text": text,
		"Link": url
	}
	db.child(session['id']).push(data)
	return url, 201