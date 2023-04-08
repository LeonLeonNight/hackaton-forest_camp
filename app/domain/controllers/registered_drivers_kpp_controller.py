from flask import request
from flask_restx import Resource

from app.domain.dto.registered_drivers_kpp_dto import Registered_drivers_kppDto
from app.domain.services.registered_drivers_kpp_service import (
    get_all_registered_drivers_kpps, delete_registered_drivers_kpp
)


api = Registered_drivers_kppDto.api
_registered_drivers_kpp = Registered_drivers_kppDto.registered_drivers_kpp


@api.route('/')
class Registered_drivers_kppList(Resource):
    @api.doc(description='list_of_all_goods_in_registered_drivers_kpp', tags=['Registered_drivers_kpp'])
    @api.marshal_list_with(_registered_drivers_kpp, envelope='data')
    def get(self):        
        return get_all_registered_drivers_kpps()

    @api.response(201, 'Success')
    @api.doc(description='create a new Kpp', tags=['Kpp'])
    @api.expect(_registered_drivers_kpp, validate=True)
    def delete(self):
        driver_id = request.json['id'] # тут может быть ошибка
        return delete_registered_drivers_kpp(driver_id)
