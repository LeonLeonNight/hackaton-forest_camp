from flask_restx import Namespace, fields


class KppDto:
    api = Namespace('kpp', description='')
    kpp = api.model('kpp',{
        'name': fields.String(required=True)
    })