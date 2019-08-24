# SERVICES
from app.services.get_local_coord_service import GetLocalCoordService
from app.handlers.intent_handler import IntentHandler
from app.handlers.weather_forecast_handler import WeatherForecastHandler
from flask import current_app


class IntentForecastMiddleware(object):

    @classmethod
    def get_forecast_based_on_intent(cls, intent):
        # get location
        location = IntentHandler.get_intent_location(intent)
        latitude, longitude = GetLocalCoordService(location).call()

        # get timedelta
        (start, end) = IntentHandler.get_intent_timedelta(intent)
        
        display_name = intent.intent.display_name

        if display_name in current_app.config.get('LOCATION_INTENTS'):
            forecast = WeatherForecastHandler.get_location_forecast(latitude, longitude, end, start)

        elif display_name in current_app.config.get('LOCATION_AND_PARAMS_INTENTS'):
            parameters = IntentHandler.get_intent_parameters(intent)
            forecast = WeatherForecastHandler.get_location_parameters(latitude, longitude, parameters, end, start)

        return forecast
        