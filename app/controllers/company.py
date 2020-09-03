from app import app,db
from flask import Flask, render_template, request, redirect, url_for, flash, session
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
            
            flash("Employee inserted successfully")

            return redirect(url_for('Index'))
        else:
            flash("Wrong password")
            return redirect(url_for('signup'))
    else:
        return redirect(url_for('signup'))

@app.route("/signin", methods = ['POST'])
def signin():
    if request.method == 'POST':
        session.pop('company_id', None)
        email = request.form["email"]
        password = request.form["password"]

        company = Company.query.filter_by(email = email).first()
        if company and company.password == password:
            session['company_id'] = company.id
            return redirect(url_for('main'))
        else:
            flash("Invalid Login")
            return redirect(url_for('Index'))