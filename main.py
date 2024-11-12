import requests
import datetime as dt

APP_ID = "3c5c0ee9"
API_KEY = "db0c282d630500a140fa612f17eab98e"
NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/0fd8b882fdcc644ed28a11adcf6f5b4c/myWorkouts/workouts"

# ------------------------------ nutritionix ------------------------------
# answer = input("Describe your today's exercise: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

data = {
    "query": "running for 10 minutes",  # Example plain text input for exercise
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
print("exercise:", exercise, duration, calories)

# ------------------------------ sheety ------------------------------

response = requests.get(url="https://api.sheety.co/0fd8b882fdcc644ed28a11adcf6f5b4c/myWorkouts/workouts/2")
response.raise_for_status()
data = response.json()

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
MY_TOKEN = ""
headers = {
    "Authorization": f"Bearer {MY_TOKEN}"
}

post_response = requests.post(url=SHEETY_ENDPOINT, json=json_data, auth=("", ""))
# post_response = requests.post(url=SHEETY_ENDPOINT, json=json_data, headers=headers)
post_response.raise_for_status()
print(response.text)
