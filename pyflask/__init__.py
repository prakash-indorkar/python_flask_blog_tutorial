from flask_bcrypt import Bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = "3f92df2c905713543cf034de12162279"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db: SQLAlchemy = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager: LoginManager = LoginManager(app)
login_manager.login_view ='login'
login_manager.login_message_category = 'info' #info is css class from bootstrap

from pyflask import routes