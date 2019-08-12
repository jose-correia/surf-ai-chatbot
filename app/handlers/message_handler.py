# SERVICES
from app.services.dialogflow.detect_intent_service import DetectIntentService
import requests


class MessageHandler(object):
    
    @classmethod
    def send_message(cls, user_id, message):
        response = {
                'recipient': {'id': user_id},
                'message': {
                    'text': message
                }
            }

        access_token = current_app.config.get('ACCESS_TOKEN')
        
        r = requests.post(
            'https://graph.facebook.com/v2.6/me/messages?access_token=' + access_token, json=response)
