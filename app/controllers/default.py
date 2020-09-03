from app import app
from flask import Flask, render_template, session
from app.models.tables import Employee
from app.controllers import default

@app.route("/")
def Index():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")
