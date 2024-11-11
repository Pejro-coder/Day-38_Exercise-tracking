import requests

APP_ID = "3c5c0ee9"
API_KEY = "db0c282d630500a140fa612f17eab98e"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

data = {
    "query": "ran 10 kilometers",  # Example plain text input for exercise
    "weight_kg": 70,
    "height_cm": 174,
    "age": 33
}

response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", headers=headers, json=data)
response.raise_for_status()
data = response.json()

print(data)
