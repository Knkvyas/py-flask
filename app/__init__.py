from flask import Flask

from config import app_config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(my_path, '../uploads')


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = 'hello'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile(os.path.join(my_path, '../config.py'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app


# configuring the Flask app and SQLAlchemy
app = create_app(config_name="config")
db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app)

# running the Flask App in debugging mode
#if __name__ == "__main__":
 #   app.run(debug=True)

from app import models, routes

