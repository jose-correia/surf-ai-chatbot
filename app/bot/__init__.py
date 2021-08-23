from flask import Blueprint
from flask_restful import Api
from .resources import BeachWeather, ReceiveMessengerEvent, MessengerWebhookVerification, Privacy, Index, SupportedLocations, SupportedParameters

bp_surf_bot = Blueprint('surf_bot', __name__, url_prefix='/surf_bot')

api = Api(bp_surf_bot)


# Routes
api.add_resource(BeachWeather, '/beach', endpoint='beach_weather')
api.add_resource(SupportedLocations, '/locations', endpoint='locations')
api.add_resource(SupportedParameters, '/parameters', endpoint='parameters')
api.add_resource(ReceiveMessengerEvent, '/messenger_webhook', endpoint='receive_messenger_event')
api.add_resource(MessengerWebhookVerification, '/webhook', endpoint='webhook_verification')
api.add_resource(Privacy, '/privacy', endpoint='privacy')
api.add_resource(Index, '/', endpoint='index')

