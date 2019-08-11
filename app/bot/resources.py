from flask_restful import Resource
from flask import request, Response, current_app
import json
import requests

import logging
logger = logging.getLogger(__name__)


def handle_message(user_id, user_message):
    # DO SOMETHING with the user_message ... ¯\_(ツ)_/¯
    return f"Hello {user_id} ! You just sent me : {user_message}"

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
            response = {
                'recipient': {'id': user_id},
                'message': {}
            }
            logger.error(user_message)
            response['message']['text'] = handle_message(user_id, user_message)

            access_token = current_app.config.get('ACCESS_TOKEN')
            r = requests.post(
                'https://graph.facebook.com/v2.6/me/messages?access_token=' + access_token, json=response)
        return Response(response="EVENT RECEIVED",status=200)


class ReceiveDevEvent(Resource):

    def post(self):
        # custom route for local development
        data = json.loads(request.data.decode('utf-8'))

        logger.error('Dev Event')

        user_message = data['entry'][0]['messaging'][0]['message']['text']
        user_id = data['entry'][0]['messaging'][0]['sender']['id']
        response = {
            'recipient': {'id': user_id},
            'message': {'text': handle_message(user_id, user_message)}
        }
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
