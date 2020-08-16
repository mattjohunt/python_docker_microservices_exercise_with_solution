from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=('mysql+pymysql://root:admin@mysql:3306/inventory')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = getenv('FLASK_SECRETKEY')

db = SQLAlchemy(app)

from application import routes