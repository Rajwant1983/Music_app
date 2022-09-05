from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

d = SQLAlchemy(application)

from routes import *

if __name__ == '__main__':
    application.run(debug=True,host='0.0.0.0',port='8085')


# Run web server using this file