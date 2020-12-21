from flask import Flask, session, request, Blueprint, jsonify
import pyrebase
from difflib import SequenceMatcher

image_blueprint = Blueprint('image_blueprint',__name__)

config = {
	"apiKey": "AIzaSyAhrOEolzpYMXYit0LWWhxmSC9zMieo6TM",
    "authDomain": "shopifyproject-e8627.firebaseapp.com",
    "databaseURL": "https://shopifyproject-e8627-default-rtdb.firebaseio.com",
    "projectId": "shopifyproject-e8627",
    "storageBucket": "shopifyproject-e8627.appspot.com",
    "messagingSenderId": "771306858953",
    "appId": "1:771306858953:web:010b5ce5392cf40d5b6018"
}

firebase = pyrebase.initialize_app(config)
@image_blueprint.route('/images',methods = ['GET'])
def list_all_images():
	image_links = []
	if(session.get('id') == None):
		return 'Need to login first', 400
	db = firebase.database()
	values = db.child(session['id']).get()
	for val in values.each():
		if(val.val().get('Link') != None):
			image_links.append((val.val()['title'], val.val()['Text']))
	return jsonify(image_links), 200


@image_blueprint.route('/images/<name>/<description>', methods=['GET'])
def search_an_image(name, description):
	images = []
	if(session.get('id')==None):
		return 'Login Please', 400
	db = firebase.database()
	vals = db.child(session['id']).get()
	for val in vals.each():
		if(val.val().get('Link')!= None):
			if(len(description) !=  0):
				name_ratio = SequenceMatcher(None, val.val()['title'],name).ratio()
				description_ratio = SequenceMatcher(None, val.val()['Text'],description).ratio()
				ratio = (name_ratio+description_ratio)/2
			else:
				ratio = SequenceMatcher(None,val.val()['title'],name).ratio()
			if(ratio >0.5):
				images.append((val.val()['Link'],val.val()['title'], ratio))
	return jsonify(images),200


