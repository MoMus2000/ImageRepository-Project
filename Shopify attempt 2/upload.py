from flask import Flask, request, session, Blueprint
import pyrebase
config = {
	"apiKey": "AIzaSyAhrOEolzpYMXYit0LWWhxmSC9zMieo6TM",
    "authDomain": "shopifyproject-e8627.firebaseapp.com",
    "databaseURL": "https://shopifyproject-e8627-default-rtdb.firebaseio.com",
    "projectId": "shopifyproject-e8627",
    "storageBucket": "shopifyproject-e8627.appspot.com",
    "messagingSenderId": "771306858953",
    "appId": "1:771306858953:web:010b5ce5392cf40d5b6018"
}


upload_blueprint = Blueprint('upload_blueprint', __name__)


#Add an image to storage and put the link into the data base according to the user
@upload_blueprint.route("/upload", methods = ["GET"])
def uploadSingleImage():
	if(session.get('id') == None):
		return 'Please Login First', 401
	firebase = pyrebase.initialize_app(config)
	auth = firebase.auth()
	db = firebase.database()
	data = {
		'LINK': 'putas@123.com'
	}
	db.child(session['id']).push(data)
	val = db.child(session['id']).get()
	for obj in val.each():
		# print(obj.key())
		print(obj.val())
	return 'Done', 200



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