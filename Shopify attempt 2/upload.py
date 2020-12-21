from flask import Flask, request, session, Blueprint
import pyrebase
import uuid
from constant import config


upload_blueprint = Blueprint('upload_blueprint', __name__)


#Add an image to storage and put the link into the data base according to the user
@upload_blueprint.route("/upload", methods = ["POST"])
def uploadSingleImage():
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


def uploadMultipleImages():
	if(session.get['id'] == None):
		return 'Please Login First', 401
	return 'Done',201



#When Iterating through Database 
#We use the following code to add an image link
# db = firebase.database()
	# data = {
		# 'LINK': 'putas@123.com'
	# }
	# db.child(session['id']).push(data)
	# val = db.child(session['id']).get()
	# for obj in val.each():
		# print(obj.key())
	# print(obj.val())
#{'type': 'normal', 'user': 'Haramillo'}
#{'LINK': '123@123.com'}.                   // OUTPUT THAT WE GET IN THE END
#{'LINK': 'putas@123.com'}
#{'LINK': 'putas@123.com'}
#{'LINK': 'putas@123.com'}