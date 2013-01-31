# manu
## Everybody's a critic

## Setting up

### You got pip

```
pip install -r requirements.txt
```

### You don't got pip

Get *pip* or install *flask* and *cloudinary* on your own.
If you need *pip* for windows search for *Cristoph Geolke Python* on Google.

## Running 

### Full dev environment

1. Install *heroku-toolbelt* and get a *heroku* username and password, and get a collaboration on the app.
2. Login to *heroku*: `heroku login`
2. Clone repo: `git clone https://github.com/yoavram/manu.git`
3. Add heroku remote: `heroku git:remote -a manumanu`
4. Create a local `.env` files with the configuration: `heroku config -s | grep CLOUD >> .env`
5. Add a debug variable to the `.env` file: `echo "DEBUG=True" >> .env`
6. Run the server using *Foreman*: `foreman start`

### Without using *heroku*

Without *heroku* you won't be able to upload images to *cloudinary*.

2. Clone repo: `git clone https://github.com/yoavram/manu.git`
3. Run using *python*: `python image_server.py`


