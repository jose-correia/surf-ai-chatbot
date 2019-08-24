# SERVICES
import requests
import os


class WeatherForecastHandler(object):
    _base_url = os.environ.get('STORMGLASS_URL')
    _headers = {'Authorization': os.environ.get('STORMGLASS_API_KEY')}

    @staticmethod
    def get_location_forecast(self, latitude, longitude, time, end, start):

        params = [{'waveHeight', 'airTemperature'}]

        url = f'{self._base_url}?lat={latitude}&lng={longitude}&start={start}&end={end}'

        logger.info(url)

        response = requests.get(url, headers=self._headers, params=params)

        if response.status_code == 200:
            return response.json()

    @staticmethod
    def get_location_parameters(self, latitude, longitude, parameters, end, start):

        url = f'{self._base_url}?lat={latitude}&lng={longitude}&start={start}&end={end}'
    
        response = requests.get(url, headers=self.self._headers, params=parameters)

        if response.status_code == 200:
            return response.json()

    # @staticmethod
    # def get_location_forecast_interval(self, latitude, longitude, time):

    