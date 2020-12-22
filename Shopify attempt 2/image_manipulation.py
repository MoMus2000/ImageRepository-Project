from flask import Flask, session, request, Blueprint, send_file
import cv2
from PIL import Image, ImageEnhance
from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from os import remove
from io import BytesIO



image_manipulation_blueprint = Blueprint('image_manipulation_blueprint',__name__)

"""
Method: Resize an Image
Request: POST
USE : Upload Image, Resize to your liking and download directly
"""

@image_manipulation_blueprint.route('/image/resize/<height>/<width>', methods=['POST'])
def image_resize(height,width):
	img = Image.open(request.files.get('image').stream)
	img = img.resize((int(width),int(height)), Image.ANTIALIAS)
	img_io = BytesIO()
	if (img.mode == "JPEG"):
		img.save(img_io, format='JPEG', quality=100)
	elif( img.mode in ["RGBA", "P"]):
		img = img.convert("RGB")
		img.save(img_io, format='JPEG', quality=100)
	img_io.seek(0)
	return send_file(img_io, as_attachment=True,mimetype='image/jpeg',attachment_filename='logo.png'),201

"""
Method: grayscale an Image
Request: POST
USE : Upload Image, grayscale and download directly
"""

@image_manipulation_blueprint.route('/image/gray', methods=['POST'])
def image_grayscale():
	img = Image.open(request.files.get('image').stream).convert('L')
	img_io = BytesIO()
	if (img.mode == "JPEG"):
		img.save(img_io, format='JPEG', quality=100)
	elif( img.mode in ["RGBA", "P"]):
		img = img.convert("RGB")
		img.save(img_io, format='JPEG', quality=100)
	else:
		img.save(img_io, format='JPEG',quality=100)
	img_io.seek(0)
	return send_file(img_io, as_attachment=True,mimetype='image/jpeg',attachment_filename='logo.png'),201

"""
Method: change quality of an Image
Request: POST
USE : Upload Image, change quality and download directly
"""

@image_manipulation_blueprint.route('/image/quality/<percent>', methods=['POST'])
def image_quality(percent):
	img = Image.open(request.files.get('image').stream)
	img_io = BytesIO()
	if (img.mode == "JPEG"):
		img.save(img_io, format='JPEG', quality=int(percent))
	elif( img.mode in ["RGBA", "P"]):
		img = img.convert("RGB")
		img.save(img_io, format='JPEG', quality=int(percent))
	else:
		img.save(img_io, format='JPEG',quality=int(percent))
	img_io.seek(0)
	return send_file(img_io, as_attachment=True,mimetype='image/jpeg',attachment_filename='logo.png'),201

"""
Method: change contrast of an Image
Request: POST
USE : Upload Image, change contrast and download directly
"""

@image_manipulation_blueprint.route('/image/contrast/<value>', methods=['POST'])
def image_contrast(value):
	img = Image.open(request.files.get('image').stream)
	contrast = ImageEnhance.Contrast(img)
	img = contrast.enhance(int(value))
	img_io = BytesIO()
	if (img.mode == "JPEG"):
		img.save(img_io, format='JPEG', quality=100)
	elif( img.mode in ["RGBA", "P"]):
		img = img.convert("RGB")
		img.save(img_io, format='JPEG', quality=100)
	else:
		img.save(img_io, format='JPEG',quality=100)
	img_io.seek(0)
	return send_file(img_io, as_attachment=True,mimetype='image/jpeg',attachment_filename='logo.png'),201
