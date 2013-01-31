# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, request, render_template, redirect, Response, url_for
import os
import cloudinary, cloudinary.uploader

# add environment variables using 'heroku config:add VARIABLE_NAME=variable_name'
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
# Cloudinary
CLOUDINARY_URL = os.environ.get("CLOUDINARY_URL")

# init & configure app
app = Flask(__name__)
app.config.from_object(__name__)  


def get_image_url(image_id, image_format):
        image_url = cloudinary.utils.cloudinary_url(image_id)[0] + '.' + image_format
        return image_url 


def add_image(image):
	params = cloudinary.uploader.build_upload_params()
	json_result = cloudinary.uploader.call_api("upload", params, file=image.stream)
    	return json_result['public_id'], json_result['format']


@app.route("/",  methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template("index.html")
	else:
		image = request.files['image']
		if not image.filename:
			return render_template("message.html", message_title="Bad form", message_body="Please provide an image file")	
		image_id, image_format = add_image(image)
		if not image_id:
			return render_template("message.html", message_title="Image upload failed")
		image_url=get_image_url(image_id,image_format)
		if not image_url:
			return render_template("message.html", message_title="Image lookup failed") 
		return render_template("image.html", image_url=image_url)


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5001))
	app.run(host='0.0.0.0', port=port, debug=app.debug)
	print "** Server shutdown"
