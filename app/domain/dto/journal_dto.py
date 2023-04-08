from flask_restx import Namespace, fields
from app.myapp import db


class JournalDto:
    api = Namespace('journal', description='')
    journal = api.model('journal',{
        'pass_number': fields.String(required=True),
        'auto_number': fields.String(required=False),
        'driver':fields.String(required=True),
        'client_name': fields.String(required=False),
        'goods_name' : fields.String(required=False),
        'count': fields.Float(required=True),
        'measurement_system_type': fields.String(required=False),
    })