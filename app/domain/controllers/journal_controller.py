from flask import request
from flask_restx import Resource

from app.domain.dto.journal_dto import JournalDto
from app.domain.services.journal_service import (get_all_journals)


api = JournalDto.api
_journal = JournalDto.journal


@api.route('/')
class JournalList(Resource):
    @api.doc(description='list_of_all_goods_in_journal', tags=['Journal'])
    @api.marshal_list_with(_journal, envelope='data')
    def get(self):        
        return get_all_journals()

    # @api.response(201, 'Success')
    # @api.doc(description='create a new Journal', tags=['Journal'])
    # @api.expect(_journal, validate=True)
    # def post(self):
    #     data = request.json
    #     return create_journal(data)

