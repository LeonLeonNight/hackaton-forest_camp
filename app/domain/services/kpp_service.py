from app.myapp import db
from app.domain.entity.kpp import Kpp


def create_kpp(data):
    kpp = Kpp.query.filter_by(name=data['name']).first()
    if not kpp:
        new_kpp = Kpp(
            name=data['name']
        )
        save_changes(new_kpp)
        response_object = {
            'status': 'success',
            'message': 'Successfully created.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Kpp already exists.',
        }
        return response_object, 409

def save_changes(data):
    db.session.add(data)
    db.session.commit()