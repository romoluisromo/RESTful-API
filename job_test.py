from flask import Flask
from flask_restful import Resource, Api
from waitress import serve
import requests
import json

app = Flask(__name__)
api = Api(app)

class JobTest(Resource):

    def __init__(self):
        pass
    
    def get(self):

        id_list = []
        number_of_ids = 0

        while number_of_ids < 25:

            response_api = requests.get('https://api.chucknorris.io/jokes/random')
            data = response_api.text
            parse_json = json.loads(data)
            id = parse_json['id']
            id_list.append(id)
            id_set = set(id_list)
            number_of_ids = len(id_set)
        id_list = list(id_set)

        return id_list

api.add_resource(JobTest, '/api/jobtest/live-coding')

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)



