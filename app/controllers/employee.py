from app import app,db
from flask import Flask, render_template, request, redirect, url_for, flash, session
from app.models.tables import Employee
from app.controllers import default

@app.route("/main")
def main():
    all_data = Employee.query.filter_by(company_id = session['company_id']).all()
    return render_template("index.html", employees = all_data)

@app.route("/addEmployee", methods = ['POST'])
def addEmployee():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        employee = Employee(name, email, phone, session['company_id'])
        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('main'))
    else:
        return redirect(url_for('main'))

@app.route("/update", methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Employee.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']

        db.session.commit()

        flash("Employee updated sucessfully")

        return redirect(url_for('main')) 

@app.route("/delete/<id>/", methods = ['GET', 'POST'])
def delete(id):
    my_data = Employee.query.get(id)
    db.session.delete(my_data)
    db.session.commit()

    flash("DEleted successfully")
    return redirect(url_for('main'))
