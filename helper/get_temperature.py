import requests
from helper.get_dates import get_dates
from helper.create_dataframe import create_df
from helper.temperature_to_sheet import temperature_to_sheet
from tkinter import messagebox


# FMI API endpoint URL
url = "https://opendata.fmi.fi/wfs"

def get_temperatures():
    """ The function uses FMI stored query to fetch daily average temperature from
    the city that is determined in the 'params' variable, key 'place'.
    
    Calls the get_dates function in helper.get_dates module to read existing
    temperature data in users spreadsheet.
    
    If temperature data doesn't exist from the day before or earlier, sends an API
    request for temperature data from FMI API between the day after the last existing
    day and the day before current day. Then uses create_df function to parse the
    XML data and uses temperature_to_sheet function to append new data into the
    spreadsheet.

    Will not send API request if data from day before already exists.
    
    Pop-up messages:
    - 'Error': Will show an error message if request to FMI API is unsuccessful. 
    - 'No new data': If all available data is in the spreadsheet, shows a message.
    - 'Success': Shows the message if data was successfully added.
    """
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
            new_temperatures = create_df(response)
            temperature_to_sheet(new_temperatures)

            message = "Temperature data updated"
            messagebox.showinfo("Success", message)
            
        else:
            # print(f"Failed to retrieve data: {response.status_code}")
            message = "Failed to retriece temperature data, please try again"
            messagebox.showinfo("Error", message)
    
    else:
        message = "All temperature data is already up-to-date"
        messagebox.showinfo("No new data", message)

