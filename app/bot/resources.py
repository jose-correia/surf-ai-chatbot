from flask_restful import Resource
from flask import request, Response, current_app
import json


def handle_message(user_id, user_message):
    # DO SOMETHING with the user_message ... ¯\_(ツ)_/¯
    return "Hello "+user_id+" ! You just sent me : " + user_message

class WebhookVerification(Resource):

    def get(self):
        if request.args.get('hub.verify_token') == current_app.config.get('WEBHOOK_VERIFICATION_TOKEN'):
            return request.args.get('hub.challenge')

        return "Failed to validate"


class ReceiveEvent(Resource):

    def post(self):
        data = json.loads(request.data.decode('utf-8'))

        for entry in data['entry']:
            user_message = entry['messaging'][0]['message']['text']
            user_id = entry['messaging'][0]['sender']['id']
            response = {
                'recipient': {'id': user_id},
                'message': {}
            }
            response['message']['text'] = handle_message(user_id, user_message)
            r = request.post(
                'https://graph.facebook.com/v2.6/me/messages/?access_token=' + access_token, json=response)
        return Response(response="EVENT RECEIVED",status=200)


class ReceiveDevEvent(Resource):

    def post(self):
        # custom route for local development
        data = json.loads(request.data.decode('utf-8'))

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
