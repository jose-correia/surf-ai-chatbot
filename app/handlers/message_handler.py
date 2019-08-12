# SERVICES
from app.services.dialogflow.detect_intent_service import DetectIntentService


class MessageHandler(object):
    @classmethod
    def handle_message(cls, user_id, message):

        detected_intent = DetectIntentService(user_id, message, 'en').call()
        
        # send intent name to IntentHandler
            # intent handler builds params and location based on the detected intent
            # call Stormglass API with detected params and location
        
        # Answer with the intent.fullfilment_text
        # Answer with the data from Stormglass

        # location = detected_intent.parameters.fields['Locations']
        return detected_intent.fulfillment_text