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

        if date_entity is None
            date_entity = 'today'

        if time_entity is None:
            time_entity = 'all day'

        start = EntityTimestampConverter().get_start_timestamp(date_entity, time_entity)
        end = EntityTimestampConverter().get_end_timestamp(date_entity, time_entity)

        return (start, end)

    @classmethod
    def get_forecast_based_on_intent(intent):

        location = self.get_intent_location(intent)
        latitude, longitude = GetLocalCoordService(location).call()

        display_name = intent.intent.display_name

        (start, end) = self.get_intent_timedelta(intent)

        if display_name in current_app.config.get('LOCATION_INTENTS'):
            forecast = WeatherForecastHandler.get_location_forecast(latitude, longitude, end, start)

        elif display_name in current_app.config.get('LOCATION_AND_PARAMS_INTENTS'):
            parameters = self.get_intent_parameters(intent)
            forecast = WeatherForecastHandler.get_location_parameters(latitude, longitude, parameters, end, start)

        return forecast
        