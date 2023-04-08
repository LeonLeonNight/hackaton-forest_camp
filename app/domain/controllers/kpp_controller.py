from flask import request
from flask_restx import Resource

from app.domain.dto.kpp_dto import KppDto
from app.domain.services.kpp_service import (
    create_kpp
)


api = KppDto.api
_kpp = KppDto.kpp


@api.route('/')
class KppList(Resource):
    @api.response(201, 'Success')
    @api.doc(description='create a new Kpp', tags=['Kpp'])
    @api.expect(_kpp, validate=True)
    def post(self):
        data = request.json
        return create_kpp(data)
