import requests


class Nutritionix:
    def __init__(self):
        self.nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

        self.nutritionix_headers = {
            "x-app-id": "d500e81b",
            "x-app-key": "22ca16fdf8a3a56b1e03ccbd28f4474d"
        }

    def post_nutritionix_data(self, query):
        nutritionix_body = {
            "query": query
        }
        response = requests.post(self.nutritionix_endpoint, json=nutritionix_body, headers=self.nutritionix_headers)
        print(response.json())
        return response.json()