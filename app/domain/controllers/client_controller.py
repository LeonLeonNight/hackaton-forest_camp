from flask import request
from flask_restx import Resource

from app.domain.dto.client_dto import ClientDto
from app.domain.services.client_service import (
    create_client
)


api = ClientDto.api
_client = ClientDto.client


@api.route('/')
class ClientList(Resource):
    @api.response(201, 'Success')
    @api.doc(description='create a new Client', tags=['Client'])
    @api.expect(_client, validate=True)
    def post(self):
        data = request.json
        return create_client(data)
