from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from routes.test import TestBot


APP = Flask(__name__)
API = Api(APP)

def create_app(config, **kwargs):
    """
    Flask App factory function
    """
    APP.config.from_object(config)
    API.add_resource(TestBot, '/test/bot',methods = ['POST'] ,endpoint='TEST_BOT')
    CORS(APP)
    return APP

