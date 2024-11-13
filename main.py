import os

import requests
import datetime as dt
from dotenv import load_dotenv

load_dotenv("C:/Users/peter/EnvironmentVariables/.env")

NUTRI_APP_ID = os.getenv("NUTRI_APP_ID")
NUTRI_API_KEY = os.getenv("NUTRI_API_KEY")
NUTRI_ENDPOINT = os.getenv("NUTRI_ENDPOINT")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")


# ------------------------------ nutritionix ------------------------------
answer = input("Describe your today's exercise: ")

headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_API_KEY,
    "Content-Type": "application/json"
}

data = {
    "query": answer,
    "weight_kg": 70,
    "height_cm": 174,
    "age": 33
}

response = requests.post(url=NUTRI_ENDPOINT, headers=headers, json=data)
response.raise_for_status()
data = response.json()
print(data)

# extract the data from the return json file
exercise = data["exercises"][0]["name"].title()
duration = round(data["exercises"][0]["duration_min"], 0)
calories = round(data["exercises"][0]["nf_calories"], 0)
# print("exercise:", exercise, duration, calories)

# ------------------------------ sheety ------------------------------
today_date = dt.datetime.now().strftime("%d/%m/%Y")
current_time = dt.datetime.now().strftime("%H:%M:%S")

json_data = {
    "workout": {
        "date": today_date,
        "time": current_time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}

headers = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
response.raise_for_status()
data = response.json()

# post_response = requests.post(url=SHEETY_ENDPOINT, json=json_data, auth=("Peter", "Peter3211213"))
post_response = requests.post(url=SHEETY_ENDPOINT, json=json_data, headers=headers)
post_response.raise_for_status()
