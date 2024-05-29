import requests
import os
from requests.auth import HTTPBasicAuth
from datetime import datetime
API_KEY=os.environ.get("ENV_NIX_API_KEY")
APP_ID=os.environ.get("ENV_NIX_APP_ID")



GENDER = 'male'
WEIGHT_KG = 60
HEIGHT_CM = 165
AGE = 19

sheety_end_point=os.environ.get("ENV_SHEETY_ENDPOINT")
headers={
    "x-app-key":API_KEY,
    "x-app-id":APP_ID,
    'Content-Type':'application/json',
    'x-remote-user-id':'0'
}

payload={
    'query':input('Tell me which excersizes you did\n'),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
end_point="https://trackapi.nutritionix.com/v2/natural/exercise"

response=requests.post(url=end_point,headers=headers,json=payload)
result=response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    

    sheet_response = requests.post(sheety_end_point, json=sheet_inputs,\
                                  
             auth=(os.environ.get("ENV_SHEETY_USERNAME"),
            os.environ.get("ENV_SHEETY_PASSWORD"),)
    )
    print(f"Sheety Response: \n {sheet_response.text}")



