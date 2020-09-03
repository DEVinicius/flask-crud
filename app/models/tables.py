from app import db

class Company(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(25))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(25))
    company_id = db.Column(db.Integer)

    def __init__(self, name, email, phone, company_id):
        self.name = name
        self.email = email
        self.phone = phone
        self.company_id = company_id