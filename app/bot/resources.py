from flask_restful import Resource
from flask import request, Response, current_app
import json

from app.handlers.message_handler import MessageHandler
from app.handlers.intent_handler import IntentHandler

import logging
logger = logging.getLogger(__name__)


class WebhookVerification(Resource):

    def get(self):
        hub_mode = request.args.get('hub.mode')
        verify_token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if hub_mode == 'subscribe' and verify_token == current_app.config.get('VERIFY_TOKEN'):
            logger.error(f'Received token: {verify_token} and challenge: {challenge}')
            return Response(response=challenge, status=200)
        
        logger.error('Failed to validade')
        return Response(response="Verification failed",status=403)


class ReceiveEvent(Resource):

    def post(self):
        logger.error('Received event')
        data = json.loads(request.data.decode('utf-8'))

        for entry in data['entry']:
            user_message = entry['messaging'][0]['message']['text']
            user_id = entry['messaging'][0]['sender']['id']
            
            intent = IntentHandler.detect_intent(user_id, user_message)
            
            if intent.intent.display_name not in current_app.config.get('NO_FORECAST_RESPONSE_INTENTS'):
                forecast = IntentHandler.get_forecast_based_on_intent(intent)
            else:
                forecast = None
                
            # send intent response
            MessageHandler.send_message(user_id, intent.fulfillment_text)

            # send data
            if forecast:
                MessageHandler.send_message(user_id, forecast)

        return Response(response="EVENT RECEIVED",status=200)


class ReceiveDevEvent(Resource):

    def post(self):
        # custom route for local development
        data = json.loads(request.data.decode('utf-8'))

        logger.error('Dev Event')

        user_message = data['entry'][0]['messaging'][0]['message']['text']
        user_id = data['entry'][0]['messaging'][0]['sender']['id']
        
        intent = IntentHandler.detect_intent(user_id, user_message)

        response = intent.fulfillment_text
        return Response(
            response=json.dumps(response),
            status=200,
            mimetype='application/json'
        )


class Privacy(Resource):

    def get(self):
        # needed route if you need to make your bot public
        return "This facebook messenger bot's only purpose is to [...]. That's all. We don't use it in any other way."


class Index(Resource):

    def get(self):
        return "Hello there, I'm a facebook messenger bot."
