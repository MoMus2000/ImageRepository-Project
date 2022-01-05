from flask import Flask
from flask import Blueprint, Flask, session , request
import pyrebase
from constant import config


signup_blueprint = Blueprint('signup_blueprint', __name__)

@signup_blueprint.route('/signup', methods = ['POST'])
def signup():
	"""
	Method : Sign up new user
	<br>
	Request : POST
	<br>
	Use : Create a user on firebase and set user in the database, along with setting a session id in flask.
	"""
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

