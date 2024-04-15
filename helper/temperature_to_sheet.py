import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
from tkinter import messagebox

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import credentials_file

credentials = Credentials.from_service_account_file(credentials_file, scopes=[
        'https://spreadsheets.google.com/feeds', 
        'https://www.googleapis.com/auth/drive'
        ])

def temperature_to_sheet(new_temperatures):
    gc = gspread.authorize(credentials)
    spreadsheet_title = "Sähkönkulutus"
    spreadsheet = gc.open(spreadsheet_title)
    sheet = spreadsheet.get_worksheet(6)

    next_row = len(sheet.get()) + 1
    data = new_temperatures.values.tolist()
    row_range = f"A{next_row}"

    sheet.update(values=data, range_name=row_range)

    messagebox.showinfo("Success", "Säätiedot lisätty")  # Show success message



""" Test function with existing .csv """
# df = pd.read_csv("data/loaded_data.csv")
# temperature_to_sheet(df)
