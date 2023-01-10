import requests
import datetime
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEST = "https://api.tequila.kiwi.com/v2/search"
TEQUILA_API_KEY = "sGL4aci_FB36Z4GLcpckrLf3oqPQ5rpl"

time_frame_in_months = 6
CURRENCY = "INR"
NIGHT_FROM = 4
NIGHTS_TO = 7


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def search_flights(self, from_city, to_city, date_from, date_to):
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {"apikey": TEQUILA_API_KEY}

        query = {
            "fly_from": from_city,
            "fly_to": to_city,
            "dateFrom": date_from.strftime("%d/%m/%Y"),
            "dateTo": date_to.strftime("%d/%m/%Y"),
            "curr": CURRENCY,
            "nights_in_dst_from": NIGHT_FROM,
            "nights_in_dst_to": NIGHTS_TO,
            "flight_type": "round",
            "max_stopovers": 1
        }

        response = requests.get(url=search_endpoint, headers=headers, params=query)
        response.raise_for_status()
        try:
            results = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {to_city}.")
            return None

        flight = FlightData(
            flyFrom=results["flyFrom"],
            flyTo=results["flyTo"],
            cityFrom=results["cityFrom"],
            cityTo=results["cityTo"],
            fare=results["price"],
            to_local_departure=results["route"][0]["local_departure"],
            to_airlines=results["route"][0]["airline"],
            to_flight_number=results["route"][0]["flight_no"],
            fro_local_departure=results["route"][1]["local_departure"],
            fro_airlines=results["route"][1]["airline"],
            fro_flight_number=results["route"][1]["flight_no"]
        )
        return flight
