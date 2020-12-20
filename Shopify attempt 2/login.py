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



login_blueprint = Blueprint('login_blueprint', __name__)

@login_blueprint.route('/auth', methods = ['POST'])
def authenticate():
	try:
		# print(request.data)
		# print(request.json['username'])
		firebase = pyrebase.initialize_app(config)
		auth = firebase.auth()
		user = auth.sign_in_with_email_and_password(request.json['username']+"@Mustafa.com", request.json['password'])
		user_id = user['idToken']
		user_type = 'normal'
		user_local = user['localId']
		session['user'] = user_id
		session['type'] = user_type
		session['id'] = user_local
		# print(session['type'])
		return 'Logged in !', 201

	except Exception as e:
		return 'something went wrong', 400

	return 'Arrived at login page'

@login_blueprint.route('/admin', methods= ['POST'])
def admin_authenticate():
	try:
		firebase = pyrebase.initialize_app(config)
		auth = firebase.auth()
		if(request.json['username'] == 'Mustafa' and request.json['password'] == 'password'):
			user = auth.sign_in_with_email_and_password(request.json['username']+"@Mustafa.com", request.json['password'])
			user_id = user['idToken']
			user_type = 'admin'
			user_local = user['localId']
			session['user'] = user_id
			session['type'] = user_type
			session['id'] = user_local
			return 'Logged in as Admin', 201
	except Exception as e:
		return 'Something went wrong', 400
	return 'Done'



@login_blueprint.route('/logout',methods = ['GET'])
def logout():
	if(session.get('id') != None):
		session.clear()
		return 'Logged Out', 200
	return 'Not Logged in', 400