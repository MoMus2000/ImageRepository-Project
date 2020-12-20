from flask import Flask
from flask import Blueprint, Flask, session , request
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


signup_blueprint = Blueprint('signup_blueprint', __name__)

@signup_blueprint.route('/signup', methods = ['POST'])
def signup():
	firebase = pyrebase.initialize_app(config)
	auth = firebase.auth()
	db = firebase.database()
	try:
		if(session['user'] != None):
			return 'You need to sign out first' , 400
	except KeyError:
		try:
			email = request.json['username']+'@Mustafa.com'
			password = request.json['password']
			user = auth.create_user_with_email_and_password(email, password)
			data = {
				'user' : request.json['username'],
				'type'  : 'normal'
			}
			db.child(user['localId']).push(data)
			session['id'] = user['localId']
			print(user['localId'])
			print(session['id'])
			return 'Created', 201
		except Exception as e:
			print(e)
			return 'Already exists', 401

