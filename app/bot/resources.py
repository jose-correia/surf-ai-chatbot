from flask_restful import Resource
from flask import request, Response, current_app
import json

from app.handlers.message_handler import MessageHandler
from app.handlers.intent_handler import IntentHandler
from app.handlers.intent_forecast_middleware import IntentForecastMiddleware
from app.values.request_weather_value import RequestWeatherValue
from app.values.response_value import ResponseValue
from app.values.errors import (
    WeatherAPIError,
    LocationNotFoundError,
)

import logging
logger = logging.getLogger(__name__)


class BeachWeather(Resource):

    def post(self):
        logger.info('Requested beach weather')

        data = json.loads(request.data.decode('utf-8'))

        logger.info('Data: {}'.format(data))

        request_value = RequestWeatherValue.parse_obj(data)

        try:
            intent = IntentHandler.detect_intent(
                request_value.sender_id,
                request_value.text,
            )
            logger.info(intent)

            logger.info("Intent: {}".format(intent.fulfillment_text))

            if intent.intent.display_name in current_app.config.get('FORECAST_RESPONSE_INTENTS'):
                forecast = IntentForecastMiddleware.get_forecast_based_on_intent(intent)
                response = forecast
            else:
                response = {"error": "Intent not configured"}

            response = ResponseValue(
                intent=intent.intent.display_name,
                text=request_value.text,
                response=intent.fulfillment_text,
                data=forecast,
            ).dict()

        except (WeatherAPIError, LocationNotFoundError) as error:
            response = error.to_dict()

        return Response(
            response=json.dumps(response),
            status=200,
            mimetype='application/json'
        )


class MessengerWebhookVerification(Resource):

    def get(self):
        logger.error('Received verification request')

        hub_mode = request.args.get('hub.mode')
        verify_token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if hub_mode == 'subscribe' and verify_token == current_app.config.get('VERIFY_TOKEN'):
            logger.error(f'Received token: {verify_token} and challenge: {challenge}')
            return Response(response=challenge, status=200)

        logger.error('Failed to validade')
        return Response(response="Verification failed",status=403)


class ReceiveMessengerEvent(Resource):

    def post(self):
        logger.error('Received event')
        data = json.loads(request.data.decode('utf-8'))

        for entry in data['entry']:
            request_value = RequestWeatherValue.from_messenger_event(data)

            intent = IntentHandler.detect_intent(request_value.text, request_value.sender_id)

            if intent.intent.display_name in current_app.config.get('FORECAST_RESPONSE_INTENTS'):
                forecast = IntentForecastMiddleware.get_forecast_based_on_intent(intent)
            else:
                forecast = None

            MessageHandler.send_message(user_id, intent.fulfillment_text)

            if forecast:
                #response = BuildResponseService(forecast).call()
                MessageHandler.send_message(user_id, str(forecast))

        return Response(response="EVENT RECEIVED",status=200)


class Privacy(Resource):

    def get(self):
        # needed route if you need to make your bot public
        return "This facebook messenger bot's only purpose is to [...]. That's all. We don't use it in any other way."


class Index(Resource):

    def get(self):
        return "Hello there, I'm a facebook messenger bot."
