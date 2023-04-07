from flask_restx import Namespace, fields


class ProfileDto:
    api = Namespace('profile', description='')
    profile = api.model('profile',{
        'profile_name': fields.String(required=True),
        'email': fields.String(required=False),
        'password':fields.String(required=True),
        'public_id':fields.String(description='identifier')
    })