from package.business import auth
from flask_restx import Resource, Namespace

forecast_api = Namespace("forecast", description="API Forecast")


@forecast_api.route("")
class Customer(Resource):
    @auth.token_required
    def get(self):
        return {
            'status': True
        }


@forecast_api.route("/<int:forecast_id>")
class CustomerDetail(Resource):
    @auth.token_required
    def get(self, forecast_id):
        return {
            'status': True
        }
