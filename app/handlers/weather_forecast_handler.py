# SERVICES
from flask import current_app as app
from typing import List
from app.values.errors import WeatherAPIError
import requests
import logging


logger = logging.getLogger()


class WeatherForecastHandler(object):
    _base_url = app.config.get('STORMGLASS_URL')
    _default_parameters = app.config.get("SUPPORTED_PARAMETERS")

    def get_location_parameters(self, latitude, longitude, end, start, parameters: List[str] = []):
        if not parameters:
            parameters = []
            for key, value in self._default_parameters.items():
                parameters.append(value)

        params = ''
        for parameter in parameters:
            params = params + parameter + ","

        params = params[:len(params)-1]

        url = f'{self._base_url}?lat={latitude}&lng={longitude}&start={start}&end={end}&params={params}'

        logger.info("Requesting forecast to API url: {}".format(url))

        try:
            data = self.request(url)
        except Exception as error:
            logger.error(error)
            raise WeatherAPIError()

        return data

    def request(self, url: str):
        headers = {'Authorization': app.config.get("STORMGLASS_API_KEY")}

        response = requests.get(
            url,
            headers=headers,
        )

        if response.status_code == 402:
            headers = {'Authorization': app.config.get("STORMGLASS_API_KEY_2")}
            response = requests.get(
                url,
                headers=headers,
            )

        response.raise_for_status()

        return response.json()

    # @staticmethod
    # def get_location_forecast_interval(self, latitude, longitude, time):


