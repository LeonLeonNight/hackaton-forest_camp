from flask_restx import Namespace, fields


class ClientDto:
    api = Namespace('client', description='')
    client = api.model('client',{
        'name': fields.String(required=True)
    })