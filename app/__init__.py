# app/__init__.py

from flask_restx import Api
from flask import Blueprint

from .domain.controllers.journal_controller import api as journal_ns
from .domain.controllers.registered_drivers_kpp_controller import api as registered_drivers_kpp_ns
from .domain.controllers.kpp_controller import api as kpp_ns
from .domain.controllers.goods_controller import api as goods_ns
from .domain.controllers.client_controller import api as client_ns
from .domain.controllers.measurement_system_type_controller import api as mst_ns


blueprint = Blueprint('swagger-api', __name__, url_prefix='/swagger-ui/')

api = Api(blueprint,
          title='FLASK RESTPLUS API FOR ZINC APP',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(journal_ns, path='/journal')
api.add_namespace(kpp_ns, path='/kpp')
api.add_namespace(mst_ns, path='/mst')
api.add_namespace(goods_ns, path='/goods')
api.add_namespace(client_ns, path='/client')
api.add_namespace(registered_drivers_kpp_ns, path='/registered_drivers_kpp')