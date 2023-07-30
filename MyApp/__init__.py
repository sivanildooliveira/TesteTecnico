from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = '30as635dfd6176f06cf3f55472d490d1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

database = SQLAlchemy()
database.init_app(app)

from MyApp import apis