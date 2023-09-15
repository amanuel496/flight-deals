class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, city, iata_code, lowest_price):
        self.city = city
        self.iata_code = iata_code
        self.lowest_price = lowest_price