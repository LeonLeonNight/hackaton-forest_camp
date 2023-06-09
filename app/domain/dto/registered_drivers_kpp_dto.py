from flask_restx import Namespace, fields
from app.myapp import db


class Registered_drivers_kppDto:
    api = Namespace('registered_drivers_kpp', description='')
    registered_drivers_kpp = api.model('registered_drivers_kpp',{
        'pass_number': fields.String(required=True),
        'auto_number': fields.String(required=False),
        'status':fields.Integer(required=False)
    })

class Registered_drivers_kppListDto:
    api = Namespace('registered_drivers_kpp', description='')
    registered_drivers_list_kpp = api.model('registered_drivers_kpp',{
        'id': fields.Integer(),
        'pass_number': fields.String(required=True),
        'auto_number': fields.String(required=False),
        'status':fields.Integer(required=False)
    })