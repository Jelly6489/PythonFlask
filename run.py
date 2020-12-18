from flask import Flask, render_template, request
from flask_restful import Resource, Api
from main import app
from flask import jsonify
import pandas as pd
from flask_cors import CORS

# CORS(app, resources={r'*': {'origins': ['https://192.168.0.10:8080/api/access', 'http://192.168.0.10:8080']}})

# app.run(host='192.168.0.10', port='8080', debug=False)
app.run(host='0.0.0.0', port='8080', debug=False)
# app.run(host='127.0.0.1', port='8080', debug=False)

'''
from flask import Flask
from flask_restful import Resource, Api
 
app = Flask(__name__)
api = Api(app)
 
class Rest(Resource):
    def get(self):
        return {'rest': 'Good !'}
    def post(self):
        return {'rest': 'post success !'}
 
api.add_resource(Rest, '/api')
 
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
'''