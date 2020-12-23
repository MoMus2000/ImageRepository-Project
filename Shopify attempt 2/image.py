from flask import Flask, session, request, Blueprint, jsonify
import pyrebase
from difflib import SequenceMatcher
from constant import config

image_blueprint = Blueprint('image_blueprint',__name__)
firebase = pyrebase.initialize_app(config)




@image_blueprint.route('/images',methods = ['GET'])
def list_all_images():
	"""
	Method : List all Images
	\n
	Request: GET
	\n
	Url: '/images'
	\n
	Use : Lists all images against a particular signed in user.
	\n
	@returns : List of images
	"""
	image_links = []
	if(session.get('id') == None):
		return 'Need to login first', 403
	db = firebase.database()
	values = db.child(session['id']).get()
	for val in values.each():
		if(val.val().get('Link') != None):
			image_links.append((val.val()['title'], val.val()['Text']))
	return jsonify(image_links), 200

@image_blueprint.route('/images/<name>/<description>', methods=['GET'])
def search_an_image(name, description):
	"""
	Method : Search an Image
	\n
	Request : GET 
	\n
	@param name: name of the image
	\n
	@param description: description of the image
	\n
	Url : /images/*name/*description
	\n
	Use: Returns a list of images against a user, according to the name and description provided. 
	The provided images also have a matching ratio number, can be used by front end to show images based on 
	relevance
	
	@returns: List of matching images
	"""
	images = []
	if(session.get('id')==None):
		return 'Login Please', 403
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


