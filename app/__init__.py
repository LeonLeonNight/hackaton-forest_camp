# app/__init__.py

from flask_restx import Api
from flask import Blueprint

from .domain.controllers.profile_controller import api as profile_ns

blueprint = Blueprint('swagger-api', __name__, url_prefix='/swagger-ui/')

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(profile_ns, path='/profile')