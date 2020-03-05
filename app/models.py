from app import db


class Clients(db.Model):
    client_id = db.Column(db.Integer, primary_key=True)
    client_first_name = db.Column(db.String(32))
    client_last_name = db.Column(db.String(32))
    client_company = db.Column(db.String(32))
    client_email = db.Column(db.String(32), unique=True, index=True)
    client_password = db.Column(db.String(128))

    def __init__(self, data):
        print(data)
        self.client_first_name = data['first_name']
        self.client_last_name = data['last_name']
        self.client_company = data['company']
        self.client_email = data['email']
        self.client_password = data['password']

    def __repr__(self):
        return '{} {} {} {} {}'.format(self.client_id, self.client_first_name, self.client_last_name, self.client_email, self.client_company)
