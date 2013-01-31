from flask import Response
import simplejson
from datetime import datetime
from flask.ext.pymongo import ObjectId
import cloudinary

class MongoDocumentEncoder(simplejson.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        elif isinstance(o, ObjectId):
            return str(o)
        return simplejson.JSONEncoder(self, o)

def jsonify(*args, **kwargs):
    return Response(simplejson.dumps(dict(*args, **kwargs), cls=MongoDocumentEncoder), mimetype='application/json')

def db_name_from_uri(full_uri):
  ind = full_uri[::-1].find('/')
  return full_uri[-ind:]

def get_photo_url(photo_id, photo_format):
  photo_url = cloudinary.utils.cloudinary_url(photo_id)[0] + '.' + photo_format
	return photo_url


def get_thumbnail_url(photo_id, photo_format):
	thumbnail_url = cloudinary.utils.cloudinary_url(photo_id, width=40, crop="fill")[0] + '.' + photo_format
	return thumbnail_url
