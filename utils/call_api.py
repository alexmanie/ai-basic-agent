import os
import requests
import json
from utils.load_config import LoadConfig
from typing import List, Tuple

APPCFG = LoadConfig()

class CallApi:
    """
    A CallApi class to interact with the API.
    """

    @staticmethod
    def respond(chatbot: List, message: str) -> Tuple:
        """
        A method to call the API.

        Args:
            message (str): The message to send to the API.

        Returns:
            str: The response from the API.
        """

        data = {"question": message}

        response = requests.post(APPCFG.api_url, json=data, headers={'Content-Type': 'application/json'})
        json_response = response.text

        # parse the JSON response
        response_dict = json.loads(json_response)
        result = response_dict['message']

        # return result

        chatbot.append((message, result))
        return "", chatbot