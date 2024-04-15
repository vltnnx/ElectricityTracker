import requests
from helper.get_dates import get_dates
from helper.create_dataframe import create_df
from helper.temperature_to_sheet import temperature_to_sheet

# FMI API endpoint URL
url = "https://opendata.fmi.fi/wfs"

def get_temperatures():
    start_date, end_date = get_dates()

    if start_date[:10] <= end_date[:10]:
        params = {
            "request": "getFeature",
            "storedquery_id": "fmi::observations::weather::daily::simple",
            "place": "Turku",
            "parameters": "Temperature",
            "starttime": start_date,
            "endtime": end_date,
            "format": "json",
            "timestep": "1440" #24h
        }

        response = requests.get(url, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            # print("Response text:", response.text)
            # print("Request successful.")
            new_temperatures = create_df(response)
            temperature_to_sheet(new_temperatures)
            
        else:
            print(f"Failed to retrieve data: {response.status_code}")

        # new_temperatures = create_df(response)

        # return new_temperatures
    
    else:
        message = "All temperature data is already up-to-date."
        print(message)
        
        # return message

