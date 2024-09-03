import os
import json
from flask import Flask, request
from utils.weather_api import WeatherApi

app = Flask(__name__)

@app.route('/parse', methods=['POST'])
def parse():

    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()
        if data is None:
            return "Invalid request. JSON data not found."

        # Access the body parameter
        body_question = data.get('question')
        if body_question is None:
            return "Invalid request. 'body_param' not found in the JSON data."

        # Process the body parameter
        # TODO: Add your code here to process the body parameter
        api_result = WeatherApi.get_weather(body_question)

        # Create a JSON object
        response = {
            'message': api_result
        }

        # Convert the JSON object to a string
        response_json = json.dumps(response)

        # Return the JSON object
        return response_json    
    else:
        return 'Content-Type not supported!'
    

@app.route('/')
def hello():
    import time

    start = time.time()
    try:
        os.system('sleep 1')
        end = time.time()
        return 'Hello! in ' + str(end - start) + ' seconds.'

    except Exception as e:
        end = time.time()
        return "Error in app ------ " + str(e) + ' in ' + str(end - start) + ' seconds.'

if __name__ == '__main__':
    app.run()