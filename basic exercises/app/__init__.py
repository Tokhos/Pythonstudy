from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import current_app, g


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

from app.controllers import default

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    db = g.pop('db', None)


    from app import db
    db.init_app(app)

    return app