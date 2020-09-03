from app import app
from flask import Flask, render_template

@app.route("/")
def Index():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")