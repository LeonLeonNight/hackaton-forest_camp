import select
import uuid
import datetime
from app.myapp import db
from app.domain.entity.journal import Journal
from app.domain.entity.client import Client
from app.domain.entity.kpp import Kpp
from app.domain.entity.goods import Goods
from app.domain.entity.measurement_system_type import MeasurementSystemType


def get_all_journals():
    return Journal.query\
            .join(Client, Journal.client_id == Client.id)\
            .join(Kpp, Journal.kpp_id == Kpp.id)\
            .join(Goods, Journal.goods_id == Goods.id)\
            .join(MeasurementSystemType, Journal.measurement_system_type_id == MeasurementSystemType.id)\
            .all()
        


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