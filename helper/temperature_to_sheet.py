import gspread
from google.oauth2.service_account import Credentials

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import credentials_file

credentials = Credentials.from_service_account_file(credentials_file, scopes=[
        'https://spreadsheets.google.com/feeds', 
        'https://www.googleapis.com/auth/drive'
        ])

def temperature_to_sheet(new_temperatures):
    """ Updates the new temperature data into the spreadsheet. """
    gc = gspread.authorize(credentials)
    spreadsheet_title = "ElectricityTracker"
    spreadsheet = gc.open(spreadsheet_title)
    sheet = spreadsheet.get_worksheet(6)

    next_row = len(sheet.get()) + 1
    data = new_temperatures.values.tolist()
    row_range = f"A{next_row}"

    sheet.update(values=data, range_name=row_range)


""" Test function with existing .csv """
# import pandas as pd
# df = pd.read_csv("data/loaded_data.csv")
# temperature_to_sheet(df)
