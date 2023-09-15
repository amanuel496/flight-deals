# class FlightSearch:
#     #This class is responsible for talking to the Flight Search API.
#     def __init__(self):
#         self.flights = []
#
#     def get_data(self):
import datetime

import requests
KIWI_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
today = datetime.datetime.now().date()
tomorrow = today + datetime.timedelta(days=1)
after_six_months = today + datetime.timedelta(days=180)

headers = {
"apikey": "CbEmcSAliSbv9GmQJpgvLC0lyuiwwXvZ"
}

params = {
    "fly_from": "DEN",
    "fly_to": "ADD",
    "date_from": tomorrow,
    "date_to": after_six_months,
    "selected_cabins": "M",
    "adult_hold_bag": 1,
    "adult_hand_bag": 1,
    "curr": "USD",
    "price_to": 1281,
    "limit": 20
}

flight_data = requests.get(KIWI_ENDPOINT, params, headers=headers)
flight_data.raise_for_status()

print(flight_data.json())



# print(tomorrow)
#
# print(after_six_months)
