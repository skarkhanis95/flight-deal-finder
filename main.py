#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_data import FlightData
from dateutil import parser
from notification_manager import NotificationManager


DEPARTURE_AIRPORT_CODE = "PNQ"
TIEMFRAME = 6     # time frame in months to which search for
TO_EMAIL = "memyselfisha@gmail.com"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

print(f"Getting Data from Google Sheets - Started at {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
sheety_data = data_manager.getData()
print(f"Getting Data from Google Sheets - Finished at {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")

print(f"Updating IATA Codes - Started at {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
for data in sheety_data:
    if data["iataCode"] == "":
        city = data["city"]
        print(city)
        iataCode = flight_search.get_destination_code(city_name=city)
        data["iataCode"] = iataCode
    row_update = {
        "price": data
    }
    data_manager.updateRow(id=data["id"], data=row_update)
print(f"Updating IATA Codes - Finished at {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")


tomorrow = datetime.now() + timedelta(days=1)
six_months_from_tomorrow = tomorrow + timedelta(days=TIEMFRAME*30)

print("Searching for flights to cities in Google Sheets Now...")
flights = []
for data in sheety_data:
    flight = flight_search.search_flights(from_city=DEPARTURE_AIRPORT_CODE,
                                 to_city=data["iataCode"],
                                 date_from=tomorrow,
                                 date_to=six_months_from_tomorrow)
    if flight is not None:
        flights.append(flight)
for data in sheety_data:

    for flight in flights:
        if data['city'] == flight.arrival_city and int(flight.fare) < int(data['lowestPrice']):
            departure_airport = flight.departure_airport_code
            departure_date = parser.parse(flight.to_local_departure).strftime('%d-%m-%Y %H:%M')
            to_flight_airlines = flight.to_flight_airlines
            to_flight_number = flight.to_flight_number
            arrival_city = flight.arrival_airport_code
            price = flight.fare
            return_date = parser.parse(flight.fro_local_departure).strftime('%d-%m-%Y %H:%M')
            return_flight_airlines = flight.fro_flight_airlines
            return_flight_number = flight.fro_flight_number
            message = f"{departure_airport} to {arrival_city} on {departure_date} and return on {return_date} \n" \
                      f"Price: {price}\n" \
                      f"Onwards Flight: {to_flight_airlines} {to_flight_number}\n" \
                      f"Return Flight: {return_flight_airlines} {return_flight_number}"
            print("**********************")
            print(message)
            notification_manager.send_email(message=message, to=TO_EMAIL)
            print("**********************")






