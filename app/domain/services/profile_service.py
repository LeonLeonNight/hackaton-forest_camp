import uuid
import datetime
from app.application import db
from app.domain.entity.profile import Profile


def create_profile(data):
    profile = Profile.query.filter_by(email=data['email']).first()
    if not profile:
        new_profile = Profile(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            profile_name=data['profile_name'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_profile)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Profile already exists. Please Log in.',
        }
        return response_object, 409


def get_all_profiles():
    return Profile.query.all()


def get_profile(public_id):
    return Profile.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()