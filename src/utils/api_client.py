import json
import requests

with open("config/nameapi_config.json", "r") as f:
    config = json.load(f)

API_KEY = config["api_key"]
BASE_URL = config["base_url"]
HEADERS = config["headers"]
PRIORITY = config.get("priority", "REALTIME")

def parse_name(first_name, last_name):
    payload = {
        "context": {"priority": PRIORITY, "properties": []},
        "inputPerson": {
            "type": "NaturalInputPerson",
            "personName": {
                "nameFields": [
                    {"string": first_name, "fieldType": "GIVENNAME"},
                    {"string": last_name, "fieldType": "SURNAME"}
                ]
            },
            "gender": "UNKNOWN"
        }
    }
    payload_str = json.dumps(payload)
    response = requests.post(f"{BASE_URL}?apiKey={API_KEY}", headers=HEADERS, data=payload_str)
    return response.json()
