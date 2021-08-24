import os
from os.path import join, dirname
from datetime import timedelta
from dotenv import load_dotenv
import logging
from logging.handlers import SysLogHandler


if os.path.isfile('.env'):
    load_dotenv('.env')


class Config:
    """Base configuration"""

    APP_ENV = os.environ.get('APP_ENV', 'development')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN')
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = join(
        dirname(__file__),
        os.environ["GOOGLE_SERVICE_ACCOUNT_KEYS"],
    )

    STORMGLASS_URL = os.environ.get('STORMGLASS_URL')
    STORMGLASS_API_KEY = os.environ.get('STORMGLASS_API_KEY')
    STORMGLASS_API_KEY_2 = os.environ.get('STORMGLASS_API_KEY_2')

    DIALOGFLOW_URL = os.environ.get('DIALOGFLOW_URL')
    DIALOGFLOW_PROJECT_ID = os.environ.get('DIALOGFLOW_PROJECT_ID')
    DIALOGFLOW_CLIENT_ACCESS_TOKEN = os.environ.get(
        'DIALOGFLOW_CLIENT_ACCESS_TOKEN',
    )

    DEBUG = False
    TESTING = False

    WTF_CSRF_ENABLED = False

    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SESSION_COOKIE_NAME = 'session'

    LOCATION_INTENTS = ['Location Forecast Intent']

    LOCATION_AND_PARAMS_INTENTS = ['Specific Weather Parameters Intent']

    FORECAST_RESPONSE_INTENTS = [
        'Location Forecast Intent',
        'Specific Weather Parameters Intent',
    ]

    SUPPORTED_PARAMETERS = {
        'Current Speed': 'currentSpeed',
        'Swell Height': 'swellHeight',
        'Swell Period': 'swellPeriod',
        'Wave Height': 'waveHeight',
        'Wave Period': 'wavePeriod',
        'Air Temperature': 'airTemperature',
        'Water Temperature': 'waterTemperature',
    }

    SUPPORTED_LOCATIONS = {
        'Costa da Caparica': {
            'latitude': 38.612310,
            'longitude': -9.216585
        },
        'Carcavelos': {
            'latitude': 38.678642,
            'longitude': -9.336061
        },
        'Guincho': {
            'latitude': 28.926815,
            'longitude': -13.634419
        },
        'Ericeira': {
            'latitude': 38.966493,
            'longitude': -9.417617,
        },
        'Nazare': {
            'latitude': 39.596779,
            'longitude': -9.069571,
        },
        'Peniche': {
            'latitude': 39.361859,
            'longitude': -9.368651,
        },
        'Figueira da Foz': {
            'latitude': 40.15085,
            'longitude': -8.86179,
        },
        'Arrifana': {
            'latitude': 40.91565,
            'longitude': -8.49657,
        },
        'Sagres': {
            'latitude': 37.068012,
            'longitude': -8.830784,
        },
        "Ribeira d'Ilhas": {
            'latitude': 38.987704,
            'longitude': -9.418905,
        },
        'Amado': {
            'latitude': 37.16949527,
            'longitude': -8.90052003,
        }
    }

    @classmethod
    def init_app(cls, app):
        pass


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

    @classmethod
    def init_app(cls, app):
        super(DevelopmentConfig, cls).init_app(app)

        syslog_handler = SysLogHandler()
        syslog_handler.setLevel(logging.WARNING)
        app.logger.addHandler(syslog_handler)


class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    RQ_ASYNC = False


class StagingConfig(Config):
    """ Staging configuration"""
    DEBUG = False
    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    SESSION_COOKIE_SECURE = True


config = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
}

__all__ = ['config']
