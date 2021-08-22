import dialogflow_v2 as dialogflow
from flask import current_app as app
import logging


logger = logging.getLogger()


class DetectIntentService():
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation.

    Returns:

    """

    def __init__(self, session_id, text, language_code):
        self.text = text
        self.language_code = language_code
        self.session_id = session_id
        self.project_id = app.config.get('DIALOGFLOW_PROJECT_ID')

    def call(self) -> bool:
        session_client = dialogflow.SessionsClient()

        session = session_client.session_path(self.project_id, self.session_id)

        text_input = dialogflow.types.TextInput(
            text=self.text, language_code=self.language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        response = session_client.detect_intent(
            session=session, query_input=query_input)

        logger.info('Query text: {}'.format(response.query_result.query_text))

        logger.info('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        logger.info('Fulfillment text: {}\n'.format(
            response.query_result.fulfillment_text))

        return response.query_result
