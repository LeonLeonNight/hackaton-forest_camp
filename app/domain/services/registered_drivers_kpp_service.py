from sqlalchemy import desc
from app.myapp import db
from app.domain.entity.registered_drivers_kpp import Registered_drivers_kpp
from app.domain.entity.client import Client
from app.domain.entity.kpp import Kpp
from app.domain.entity.goods import Goods


def get_all_registered_drivers_kpps():
    return Registered_drivers_kpp.query.order_by(desc(Registered_drivers_kpp.id)).all()

def delete_registered_drivers_kpp(driver_id):
    driver = Registered_drivers_kpp.query(driver_id)
    delete_changes(driver)

    response_object = {
        'status': 'success',
        'message': 'Successfully deleted.'
    }
    return response_object, 201

def create_registered_drivers_kpp(data):
    driver = Registered_drivers_kpp.query.filter_by(pass_number=data['pass_number']).first()
    if not driver:
        new_driver = Registered_drivers_kpp(
            pass_number=data['pass_number'],
            auto_number=data['auto_number'],
            status=data['status']
        )
        save_changes(new_driver)
        response_object = {
            'status': 'success',
            'message': 'Successfully driver.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Driver already exists.',
        }
        return response_object, 409



def save_changes(data):
    db.session.add(data)
    db.session.commit()

def delete_changes(data):
    db.session.delete(data)
    db.session.commit()