import requests

ENDPOINT = "https://api.sheety.co/9a8fb9a200dc0ad0020d32ac5bb21400/flightDeals/prices"
TOKEN = "Bearer ushdfjsdhf8y43rbsdhj84yrshjdf832yrhsdcj9832sdf"
HEADERS = {
    "Authorization" : TOKEN
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def getData(self):
        response = requests.get(url=ENDPOINT, headers=HEADERS)
        if response.status_code != 200:
            response.raise_for_status()
        data = response.json()
        sheety_data = data["prices"]
        return sheety_data

    def updateRow(self, id, data):
        update_url = f"{ENDPOINT}/{id}"
        response = requests.put(url=update_url, headers=HEADERS, json=data)
        response.raise_for_status()


