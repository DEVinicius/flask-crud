from app import db

class Company(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(25))

    @property
    def is_autenticated(self):
        return True
    
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
        
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def __repr__(self):
        return f'<Company: {self.name} {self.email}'

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

    def __repr__(self):
        return f'<Employee: {self.name} {self.email} {self.phone}>'