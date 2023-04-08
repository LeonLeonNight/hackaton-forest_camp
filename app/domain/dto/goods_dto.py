from flask_restx import Namespace, fields


class GoodsDto:
    api = Namespace('goods', description='')
    goods = api.model('goods',{
        'name': fields.String(required=True)
    })