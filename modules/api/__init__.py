from flask_restx import Api
from .customer import customer
from .forecast import forecast_api

api = Api(doc="/api/doc", prefix="/api")

api.add_namespace(customer)
api.add_namespace(forecast_api)
