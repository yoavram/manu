# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, request, render_template, redirect, Response, url_for, jsonify
import os
import cloudinary, cloudinary.uploader, cloudinary.api

# add environment variables using 'heroku config:add VARIABLE_NAME=variable_name'
DEBUG = os.environ.get('DEBUG', 'True').strip() == 'True'
# Cloudinary
CLOUDINARY_URL = os.environ.get("CLOUDINARY_URL")

# init & configure app
app = Flask(__name__)
app.config.from_object(__name__)  

if app.debug:
	print "**Debug mode"
else:
	print "**Production mode:"


# Web API
@app.route("/", methods=["GET","POST"])
def index():
	if request.method == "POST":
		print "filename:", request.files['image'].filename
		result = _upload_image()
		print "result:",result
		if check_error(result): 
			return print_error(result)
		image_id, image_format, image_url = result['image_id'], result['image_format'], result['image_url']
		thumbnail_url = get_thumbnail_url(image_id, image_format)
		return render_template("image.html", image_url=image_url, thumbnail_url=thumbnail_url)
	else:
		images = _list_images()
		print images
		return render_template("index.html", images=images['images'])
	

# REST API
@app.route("/image", methods=["POST"])
def upload_image():
	return jsonify(_upload_image())

def _upload_image():
	image = request.files['image']
	if not image.filename: 
		json_error("Image file missing")	
	name = request.form['name']	
	if not name: 
		name = '.'.join(image.filename.split('.')[:-1])
	params = cloudinary.uploader.build_upload_params(public_id=name)
	json_result = cloudinary.uploader.call_api("upload", params, file=image.stream)	
	if check_error(json_result):
		return json_result
	return {	
			'image_url': json_result['url'], 
			'image_id': json_result['public_id'], 
			'image_format': json_result['format']
		}


@app.route("/listImages")
def list_images():
	return jsonify(_list_images())


def _list_images():
	result = cloudinary.api.resources()
	if check_error(result): return result
	resources = result['resources']
	resources =  [{'image_id':item['public_id'], 'image_format': item['format'], 'image_url': item['url']} for item in resources ]
	return {'images': resources}


@app.route("/image/<string:image_id>/<string:image_format>")
def get_image_url(image_id, image_format):
	return cloudinary.utils.cloudinary_url(image_id)[0] + '.' + image_format


@app.route("/thumbnail/<string:image_id>/<string:image_format>")
def get_thumbnail_url(image_id, image_format):
	return 	cloudinary.utils.cloudinary_url(image_id, width=40, crop="fill")[0] + '.' + image_format


def json_error(error_message):
	return {"error": {'message': error_message}}

def check_error(result):
	return 'error' in result

def print_error(result):
	return render_template("message.html", message_title='Error', message_body=result['error']['message'])

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))	
	app.run(host='0.0.0.0', port=port, debug=app.debug)
	print "** Server shutdown"
