import select
import uuid
import datetime
from app.application import db
from app.domain.entity.registered_drivers_kpp import Registered_drivers_kpp
from app.domain.entity.client import Client
from app.domain.entity.kpp import Kpp
from app.domain.entity.goods import Goods


def get_all_registered_drivers_kpps():
    return (Registered_drivers_kpp.query.orderby(Registered_drivers_kpp.id.desc()).all())


# def create_profile(data):
#     profile = Profile.query.filter_by(email=data['email']).first()
#     if not profile:
#         new_profile = Profile(
#             public_id=str(uuid.uuid4()),
#             email=data['email'],
#             profile_name=data['profile_name'],
#             password=data['password'],
#             registered_on=datetime.datetime.utcnow()
#         )
#         save_changes(new_profile)
#         response_object = {
#             'status': 'success',
#             'message': 'Successfully registered.'
#         }
#         return response_object, 201
#     else:
#         response_object = {
#             'status': 'fail',
#             'message': 'Profile already exists. Please Log in.',
#         }
#         return response_object, 409


# def get_profile(public_id):
#     return Profile.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()