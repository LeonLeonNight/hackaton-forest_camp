from app.myapp import db
from app.domain.entity.client import Client


def create_client(data):
    client = Client.query.filter_by(name=data['name']).first()
    if not client:
        new_client = Client(
            name=data['name']
        )
        save_changes(new_client)
        response_object = {
            'status': 'success',
            'message': 'Successfully created.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Client already exists.',
        }
        return response_object, 409

def save_changes(data):
    db.session.add(data)
    db.session.commit()