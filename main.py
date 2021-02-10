"""App starting point"""
import os

from app import create_app
from config import APP_CONFIG

ENV_CONFIG = os.getenv("ENV", "development")

APP = create_app(APP_CONFIG[ENV_CONFIG])

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=5001, debug=True)
