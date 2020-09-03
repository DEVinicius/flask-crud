from app import app
from flask import Flask, render_template, session
from app.models.tables import Employee
from app.controllers import default

@app.route("/main")
def main():
    print(session["company_id"])
    return render_template("index.html")