from flask import Blueprint
from flask_restful import Api
from .resources import ReceiveDevEvent, ReceiveEvent, WebhookVerification, Privacy, Index

bp_surf_bot = Blueprint('surf_bot', __name__, url_prefix='/surf_bot')

api = Api(bp_surf_bot)


# Routes
api.add_resource(ReceiveEvent, '/webhook', endpoint='receive_event')
api.add_resource(WebhookVerification, '/webhook', endpoint='webhook_verification')
api.add_resource(ReceiveDevEvent, '/webhook_dev', endpoint='receive_dev_event')
api.add_resource(Privacy, '/privacy', endpoint='privacy')
api.add_resource(Index, '/', endpoint='index')

