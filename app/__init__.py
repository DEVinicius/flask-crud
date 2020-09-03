from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app =  Flask(__name__)
app.secret_key = "secret key"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://vini:Ralph@2411@localhost/crud"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from app.controllers import default
from app.controllers import company
from app.controllers import employee
