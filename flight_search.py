# class FlightSearch:
#     #This class is responsible for talking to the Flight Search API.
#     def __init__(self):
#         self.flights = []
#
#     def get_data(self):
import datetime

import requests
from flight_data import FlightData

KIWI_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
KIWI_API_KEY = "CbEmcSAliSbv9GmQJpgvLC0lyuiwwXvZ"
CITY = ["ADD", "PAR", "BER", "TYO"]
FLY_FROM = "DEN"
CABIN = "M"
HOLD_BAG = 1
HAND_BAg = 1
CURRENCY = "USD"


class FlightSearch:
    def __init__(self):
        self.flight_prices = []

    def get_data(self):
        today = datetime.datetime.now().date()
        tomorrow = today + datetime.timedelta(days=1)
        after_six_months = today + datetime.timedelta(days=180)

        headers = {
            "apikey": KIWI_API_KEY
        }

        for fly_to in CITY:
            params = {
                "fly_from": FLY_FROM,
                "fly_to": fly_to,
                "date_from": tomorrow,
                "date_to": after_six_months,
                "selected_cabins": CABIN,
                "adult_hold_bag": HOLD_BAG,
                "adult_hand_bag": HAND_BAg,
                "curr": "USD",
                # "price_to": 1281,
                # "limit": 20
            }

            response = requests.get(KIWI_ENDPOINT, params, headers=headers)
            response.raise_for_status()

            city = response.json()["data"][0]["cityTo"]
            price = response.json()["data"][0]["price"]

            flight_data = FlightData(city=city, iata_code=fly_to, lowest_price=price)
            self.flight_prices.append(flight_data)

            # print(flight_data.city, " ", flight_data.iata_code, " ", flight_data.lowest_price)

# fligh_search = FlightSearch()
#
# fligh_search.get_data()
