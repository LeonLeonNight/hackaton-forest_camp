from flask import request
from flask_restx import Resource

from app.domain.dto.goods_dto import GoodsDto
from app.domain.services.goods_service import (
    create_goods
)


api = GoodsDto.api
_goods = GoodsDto.goods


@api.route('/')
class GoodsList(Resource):
    @api.response(201, 'Success')
    @api.doc(description='create a new Goods', tags=['Goods'])
    @api.expect(_goods, validate=True)
    def post(self):
        data = request.json
        return create_goods(data)
