# app/__init__.py

from flask_restx import Api
from flask import Blueprint

from .domain.controllers.journal_controller import api as journal_ns
from .domain.controllers.registered_drivers_kpp_controller import api as registered_drivers_kpp_ns

blueprint = Blueprint('swagger-api', __name__, url_prefix='/swagger-ui/')

api = Api(blueprint,
          title='FLASK RESTPLUS API FOR ZINC APP',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(journal_ns, path='/journal')
api.add_namespace(registered_drivers_kpp_ns, path='/registered_drivers_kpp')