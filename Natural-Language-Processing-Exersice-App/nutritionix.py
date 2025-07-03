import requests
import os
import dotenv

dotenv.load_dotenv()

x_app_id = os.getenv("X-APP-ID")
x_app_key = os.getenv("X-APP-KEY")


class Nutritionix:
    def __init__(self):
        self.nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

        self.nutritionix_headers = {
            "x-app-id": x_app_id,
            "x-app-key": x_app_key
        }

    def post_nutritionix_data(self, query):
        nutritionix_body = {
            "query": query
        }
        response = requests.post(self.nutritionix_endpoint, json=nutritionix_body, headers=self.nutritionix_headers)
        print(response.json())
        return response.json()