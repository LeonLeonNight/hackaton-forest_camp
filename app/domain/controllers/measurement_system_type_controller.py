from flask import request
from flask_restx import Resource

from app.domain.dto.measurement_system_type_dto import MSTDto
from app.domain.services.measurement_system_type_service import (
    create_mst
)


api = MSTDto.api
_mst = MSTDto.mst


@api.route('/')
class MstList(Resource):
    @api.response(201, 'Success')
    @api.doc(description='create a new MST', tags=['MST'])
    @api.expect(_mst, validate=True)
    def post(self):
        data = request.json
        return create_mst(data)
