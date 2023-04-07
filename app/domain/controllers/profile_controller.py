from flask import request
from flask_restx import Resource

from app.domain.dto.profile_dto import ProfileDto
from app.domain.services.profile_service import (
    get_all_profiles, create_profile, get_profile
)


api = ProfileDto.api
_profile = ProfileDto.profile


@api.route('/')
class ProfileList(Resource):
    @api.doc(description='list_of_registered_Profile', tags=['Profile'])
    @api.marshal_list_with(_profile, envelope='data')
    def get(self):        
        return get_all_profiles()

    @api.response(201, 'Success')
    @api.doc(description='create a new Profile', tags=['Profile'])
    @api.expect(_profile, validate=True)
    def post(self):
        data = request.json
        return create_profile(data)


@api.route('/<public_id>')
@api.param('public_id', 'identifier')
@api.response(404, 'Not found')
class Profile(Resource):
    @api.doc('get a Profile')
    @api.marshal_with(_profile)
    def get(self, public_id):
        profile = get_profile(public_id)
        if not profile:
            api.abort(404)
        else:
            return profile
