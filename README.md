# manu
## Everybody's a critic

## Setup and run 

### Dependencies

1. [Python](www.python.org/getit/), preferably version 2.7.3
2. The python packagge installer [pip](http://www.pip-installer.org/). If you need it for windows and can get it to work try downloading it [from here](http://www.lfd.uci.edu/~gohlke/pythonlibs/).
3. The python virtual environment manager [virtualenv](http://www.virtualenv.org/). 
4. The [heroku CLI toolbelt](https://toolbelt.heroku.com/)
5. A [heroku](http://www.heroku.com) username and password
6. To be a collaborator on the *heroku* [manumanu](http://manumanu.herokuapp.com) app.

### Setup

1. Open a command line\terminal window.
2. Login to *heroku*: `heroku login`
2. Clone repo: `git clone https://github.com/yoavram/manu.git`
3. Add heroku remote: `heroku git:remote -a manumanu`
4. Create a local `.env` file with the configuration: `heroku config -s | grep CLOUD >> .env`
5. Add a debug variable to the `.env` file: `echo DEBUG=True >> .env`
6. Add a variable to tell foreman to output print messages to console: `echo PYTHONUNBUFFERED=true >> .env`
6. Create a virtual environment using *virtualenv*: `virtualenv venv`
7. Activate the virtual environment: On linux `source venv/bin/activate/`, on windows `venv\Scripts\activate.bat`
8. Install python requirements: `pip install -r requirements.txt`

### Run

Run the server locally using *Foreman*: `foreman start`.
You could also start it via `python image_server.py` but it will not read the *heroku* configuration so you will not be connected to third-party services.

## REST API

The main API URL is `http://manumanu.herokuapp.com`, or `http://localhost:5000` if you are working locally.

### Upload image

Used to upload a single image.

- Endpoint: `/image`
- Method: `POST`
- Post data: `name`, optional, an identifier for the image
- Post files: `image`, mandatory, a single image file stream
- Returns a JSON with the following keys:
  - `image_id`: an identifier of the image. Save this to retrieve/delete the image later on. This is equal to `name` if `name was given.
  - `image_url`: the URL of the image (may change, so save the ID not the URL)
  - `image_format`: the format (i.e. `png`, `jpg`) of the image. Save this to retrieve a correct image URL later on.
See example in the form in `index.html`.

### List images
Lists the images in the server.

- Endpoint: `/listImages`
- Method: `GET`
- No data or arguments
- Returns a JSON with a list `[]` of image details (`image_id`, `image_url`, `image_format`)

### Image URL

Get the URL of an image

- Endpoint: `image/<string:image_id>/<string:image_format>`
- Method: `GET`
- Returns a string of the URL

### Image thumbnail URL

Get the URL of a thumbnail for an image

- Endpoint: `thumbnail/<string:image_id>/<string:image_format>`
- Method: `GET`
- Returns a string of the URL
