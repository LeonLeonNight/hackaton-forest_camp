from app.myapp import db
from app.domain.entity.measurement_system_type import MeasurementSystemType


def create_mst(data):
    mst = MeasurementSystemType.query.filter_by(name=data['name']).first()
    if not mst:
        new_mst = MeasurementSystemType(
            name=data['name']
        )
        save_changes(new_mst)
        response_object = {
            'status': 'success',
            'message': 'Successfully created.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Measurement already exists.',
        }
        return response_object, 409

def save_changes(data):
    db.session.add(data)
    db.session.commit()