# This file uses the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


def main():
    all_time_flight_data = DataManager()
    all_time_flight_data.get_data()

    current_flight_data = FlightSearch()
    current_flight_data.get_data()

    for i in range(len(all_time_flight_data.all_time_cheapest_flight)):
        if all_time_flight_data.all_time_cheapest_flight[i].lowest_price > current_flight_data.flight_prices[
                i].lowest_price:
            message = (f"Low price alert! Only for ${current_flight_data.flight_prices[i].lowest_price} "
                       f"to fly from Denver-DEN to {all_time_flight_data.all_time_cheapest_flight[i].city}-"
                       f"{all_time_flight_data.all_time_cheapest_flight[i].iata_code}.")
            NotificationManager(message)


if __name__ == "__main__":
    main()
