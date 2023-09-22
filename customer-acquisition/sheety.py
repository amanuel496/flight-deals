import os
import requests

SHEETY_API_ENDPOINT = os.environ.get("SHEETY_API_ENDPOINT")
SHEETY_API_AUTH = os.environ.get("SHEETY_API_AUTH")
headers = {
    "Authorization": SHEETY_API_AUTH
}


def post_data(user):
    body = {
        "user": user
    }
    response = requests.post(url=SHEETY_API_ENDPOINT, json=body, headers=headers)
    response.raise_for_status()
    print("You're in the club!")


class Sheety:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.users = []

    def get_data(self):
        users_data = requests.get(url=SHEETY_API_ENDPOINT, headers=headers)
        users_data.raise_for_status()
        self.users = users_data.json()["users"]
