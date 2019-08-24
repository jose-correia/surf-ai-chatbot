# SERVICES
from app.services.get_local_coord_service import GetLocalCoordService
from app.services.dialogflow.detect_intent_service import DetectIntentService
from app.services.dialogflow.entity_timestamp_converter import EntityTimestampConverter
from app.handlers.weather_forecast_handler import WeatherForecastHandler
from flask import current_app


class IntentHandler(object):

    @classmethod
    def detect_intent(cls, user_id, message):
        return DetectIntentService(user_id, message, 'en').call() 

    @classmethod 
    def get_intent_location(cls, intent):
        for parameter in intent.parameters.fields['Locations']:
            if parameter.string_value is not None:
                return parameter.string_value 

    @classmethod 
    def get_intent_timedelta(cls, intent):
        
        time_entity = None
        date_entity = None

        for parameter in intent.parameters.fields['Time'].list_value:
            time_entity = parameter

        for parameter in intent.parameters.fields['Date'].list_value:
            date_entity = parameter

        if date_entity is None:
            date_entity = 'today'

        if time_entity is None:
            time_entity = 'all day'

        start = EntityTimestampConverter().get_start_timestamp(date_entity, time_entity)
        end = EntityTimestampConverter().get_end_timestamp(date_entity, time_entity)

        return (start, end)

    @classmethod 
    def get_intent_parameters(cls, intent):
        parameters = []

        for parameter in intent.parameters.fields['Weather_Parameters'].list_value:
            parameters.append(parameter)

        return parameters
        