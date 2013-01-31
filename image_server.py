# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, request, render_template, redirect, Response, url_for
import os
import cloudinary, cloudinary.uploader, cloudinary.api

# add environment variables using 'heroku config:add VARIABLE_NAME=variable_name'
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
# Cloudinary
CLOUDINARY_URL = os.environ.get("CLOUDINARY_URL")

# init & configure app
app = Flask(__name__)
app.config.from_object(__name__)  

def get_photo_url(photo_id, photo_format):
        photo_url = cloudinary.utils.cloudinary_url(photo_id)[0] + '.' + photo_format
        return photo_url


def get_thumbnail_url(photo_id, photo_format):
        thumbnail_url = cloudinary.utils.cloudinary_url(photo_id, width=40, crop="fill")[0] + '.' + photo_format
        return thumbnail_url


def add_photo(photo):
	params = uploader.build_upload_params()
	json_result = uploader.call_api("upload", params, file=photo.stream)
    	return json_result['public_id'], json_result['format']

@app.route("/",  methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template("index.html")
	else:
		if 'name' not in request.form or 'image' not in request.files:
			return render_template("message.html", message_title="Bad form", message_body="Please provide image file and name for file")
		name, image = request.form['name'], request.files['image']
		image_id, image_format = add_image(image)
		if not image_id:
			return render_template("message.html", message_title="Image upload failed")
		return render_template("image.html", image_url=get_photo_url(image_id,image_format))

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5001))
	app.run(host='0.0.0.0', port=port, debug=app.debug)
	print "** Server shutdown"
