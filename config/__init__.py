"""Flask App configurations"""

import os

class Config:
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    UPLOAD_FOLDER = '/home/kamal/global_api/src/uploads'
    AUTH_SERVER_URL = 'http://rmlin-sm-web.infra.rmlconnect.net/auth/v1/validate/'

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False
    UPLOAD_FOLDER = '/home/src/worker/scripts/files/bulk_upload'
    AUTH_SERVER_URL = 'http://rmlin-sm-web.infra.rmlconnect.net/auth/v1/validate/'

APP_CONFIG = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
