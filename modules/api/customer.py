from package.business import auth
from flask import request
from flask_restx import Resource, fields, Namespace

customer = Namespace("customer", description="API Customer")


@customer.route("")
class Customer(Resource):
    @auth.token_required
    def get(self):
        return {
            'status': 200
        }


@customer.route("/<int:customer_id>")
class CustomerDetail(Resource):
    @auth.token_required
    def get(self, customer_id):
        return {
            'status': 200
        }
