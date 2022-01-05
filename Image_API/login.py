from flask import Blueprint, Flask, session , request
import pyrebase
from constant import config

login_blueprint = Blueprint('login_blueprint', __name__)






@login_blueprint.route('/auth', methods = ['POST'])
def authenticate():
	"""
	Method: authenticate user (sign in)
	<br>
	Request: POST
	<br>
	Url: '/auth'
	<br>
	Use : Returns a token which is stored along with user-type for flask session cookies
	"""
	try:
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
	"""
	Method : Admin authentication
	<br>
	Request: POST
	<br>
	Url : '/admin'
	<br>
	Use : Used to authenticate admin and set the user type as admin
	"""
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
	"""
	Method : Logout user
	<br>
	Url : '/logout'
	<br>
	Use : To eliminate sesssion cookies, so that user is unable to use apis that require access token / sesssion id.
	"""
	if(session.get('id') != None):
		session.clear()
		return 'Logged Out', 200
	return 'Not Logged in', 400