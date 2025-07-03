import requests
import os
import dotenv

dotenv.load_dotenv()

authorization = os.getenv("AUTHORIZATION")


class Sheety:
    def __init__(self):
        # End points
        self.post_endpoint = "https://api.sheety.co/932d437fd0e7958eee7c5c49709d72cf/project1/sheet1"
        self.get_endpoint = "https://api.sheety.co/932d437fd0e7958eee7c5c49709d72cf/project1/sheet1"
        # Heather
        self.headers = {
           "Authorization": authorization
        }

    def post_data(self, date, time, exercise, duration, calories):
        body = {
            "sheet1": {
                "date": date,
                "time": time,
                "exercise": exercise,
                "duration": duration,
                "calories": calories
            }
        }

        response = requests.post(self.post_endpoint, json=body, headers=self.headers)
        print(response.json())

    def get_data(self):
        response = requests.get(self.get_endpoint, headers=self.headers)
        return response.json()
