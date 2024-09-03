import os
import requests
import json
from utils.functions import run_conversation
from utils.load_config import LoadConfig

APPCFG = LoadConfig()

class WeatherApi:

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_weather(user_query: str) -> str:
        """
        A method to get the weather of a city.

        Args:
            city (str): The city to get the weather.

        Returns:
            str: The weather of the city.
        """

        # Run the conversation and print the result
        result = run_conversation(user_query)   # Parallel function call with a single tool/function defined
        
        return result