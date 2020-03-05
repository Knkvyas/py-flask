from flask import jsonify

from app.models import Clients
from app import db

class ClientDB:

    def toJSON(self, client):
        client_json = dict()
        client_json['first_name'] = client.client_first_name
        client_json['last_name'] = client.client_last_name
        client_json['password'] = client.client_password
        client_json['email'] = client.client_email
        return client_json

    def get_client_by_email(self, email):
        client = Clients.query.filter_by(client_email=email).first()
        client_json = self.toJSON(client)
        return client_json

    def create_client(self, data):
        new_client = Clients(data)
        db.session.add(new_client)
        db.session.commit()
        return data

    def check_email_exists(self, email):
        print(email)
        client = Clients.query.filter_by(client_email=email)
        if client:
            print(client)
            return True
        return False
