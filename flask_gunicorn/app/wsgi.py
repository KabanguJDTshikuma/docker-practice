from flask_gunicorn.app import app

# do some production specific things to the app
app.config['DEBUG'] = False