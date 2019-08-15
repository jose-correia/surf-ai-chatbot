

import dialogflow_v2 as dialogflow
from flask import current_app
import os

class BuilResponseService():
    """
    Based on a forecast dict, builds the response that
    will be forwarded to the client

    {
    "hours": [
        {
            "airTemperature": [
                {
                    "source": "sg",
                    "value": 16.37
                },
            ],
            "time": "2019-08-12T00:00:00+00:00",
            "waveHeight": [
                {
                    "source": "sg",
                    "value": 0.6
                },
            ]
        },
    }
    """

    def __init__(self, forecast):
        self.forecast = forecast

    def call(self) -> bool:
        
        for hour in forecast['hours']:
            for parameter in hour:
                
        return response.query_result
    