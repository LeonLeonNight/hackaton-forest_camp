from flask_restx import Namespace, fields


class MSTDto:
    api = Namespace('mst', description='')
    mst = api.model('mst',{
        'name': fields.String(required=True)
    })