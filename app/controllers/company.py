from app import app,db
from flask import Flask, render_template, request, redirect, url_for
from app.models.tables import Company
from app.controllers import default

@app.route("/insertCompany", methods = ['POST'])
def insertCompany():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        repassword = request.form["re-password"]

        if password == repassword:
            company = Company(name, email, password)
            db.session.add(company)
            db.session.commit()

            return redirect(url_for('Index'))
        else:
            return redirect(url_for('signup'))
    else:
        return redirect(url_for('signup'))