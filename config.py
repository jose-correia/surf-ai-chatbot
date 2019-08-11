import os
from datetime import timedelta
from dotenv import load_dotenv


if os.path.isfile('.env'):
    load_dotenv('.env')


class Config:
    """Base configuration"""

    APP_ENV = os.environ.get('APP_ENV', 'development')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN')
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')

    DEBUG = False
    TESTING = False

    WTF_CSRF_ENABLED = False

    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SESSION_COOKIE_NAME = 'session'


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True


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
