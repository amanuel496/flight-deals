import os
import requests
from flight_data import FlightData

SHEETY_API_ENDPOINT = os.environ.get("SHEETY_API_ENDPOINT")
SHEETY_API_AUTH = os.environ.get("SHEETY_API_AUTH")


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.all_time_cheapest_flight = []

    # Get all time cheapest flights data
    def get_data(self):
        headers = {
            "Authorization": SHEETY_API_AUTH
        }
        flight_price_data = requests.get(url=SHEETY_API_ENDPOINT, headers=headers)
        flight_price_data.raise_for_status()

        flight_price_list = flight_price_data.json()["prices"]

        for flight in flight_price_list:
            city = flight["city"]
            iata_code = flight["iataCode"]
            lowest_price = flight["lowestPrice"]
            flight_data = FlightData(city, iata_code, lowest_price)
            self.all_time_cheapest_flight.append(flight_data)
