from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '29cecf8afd6176f06bb3f55472d490d1'
if os.getenv('DATABASE_URL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view ='login'
login_manager.login_message_category = 'alert-info'

from comunidadetecnologica import models
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspection = sqlalchemy.inspect(engine)
if not sqlalchemy.engine.reflection.Inspector.has_table(inspection, "usuario"):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print("base de dados criada")
else:
    print("base de dados já existente")

from comunidadetecnologica import routes