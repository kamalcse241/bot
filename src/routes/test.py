import os
from flask_restful import Resource, request

class TestBot(Resource):
	def post(self):
		try:
			data = request.get_json()
			msg = {"recipient_id": data.get('sender'), "text": "Hi, I'm OG, your virtual guide, i'm happy to help you.."}
			headers = {"Content-Type": "application/json"}
			return msg, 200, headers
		except Exception as e:
			raise e
