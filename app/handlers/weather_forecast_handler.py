# SERVICES
from flask import current_app as app
from typing import List
from app.values.errors import WeatherAPIError
import requests
import logging


logger = logging.getLogger()


class WeatherForecastHandler(object):
    _base_url = app.config.get('STORMGLASS_URL')
    _headers = {'Authorization': app.config.get('STORMGLASS_API_KEY')}
    _default_parameters = ['currentSpeed', 'swellHeight', 'swellPeriod', 'waveHeight', 'wavePeriod', 'airTemperature', 'waterTemperature']

    def get_location_parameters(self, latitude, longitude, end, start, parameters: List[str] = []):
        if not parameters:
            parameters = self._default_parameters

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
        response = requests.get(
            url,
            headers=self._headers,
        )

        response.raise_for_status()

        return response.json()

    # @staticmethod
    # def get_location_forecast_interval(self, latitude, longitude, time):


