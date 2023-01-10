class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, flyFrom, flyTo, cityFrom, cityTo, fare, to_local_departure,
                 to_airlines, to_flight_number, fro_local_departure,
                 fro_airlines, fro_flight_number):

        self.departure_airport_code = flyFrom
        self.arrival_airport_code = flyTo
        self.departure_city = cityFrom
        self.arrival_city = cityTo
        self.fare = fare
        self.to_local_departure = to_local_departure
        self.to_flight_airlines = to_airlines
        self.to_flight_number = to_flight_number
        self.fro_local_departure = fro_local_departure
        self.fro_flight_airlines = fro_airlines
        self.fro_flight_number = fro_flight_number

