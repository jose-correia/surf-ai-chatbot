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

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = join(dirname(__file__), os.environ["GOOGLE_SERVICE_ACCOUNT_KEYS"])


    DEBUG = False
    TESTING = False

    WTF_CSRF_ENABLED = False

    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SESSION_COOKIE_NAME = 'session'

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
