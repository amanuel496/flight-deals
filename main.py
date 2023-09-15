#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager


def main():
    flight_data = DataManager()
    flight_data.get_data()

    for flight in flight_data.all_time_cheapest_flight:
        print(flight.city, " ", flight.iata_code, " ", flight.lowest_price)

if __name__ == "__main__":
    main()