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
