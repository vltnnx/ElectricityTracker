from datetime import datetime, timedelta
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

def get_dates():
    """ From the spreadsheet, fetches the last existing date for temperature 
    data. Based on the existing data, creates a start_date and end_date to use
    in the FMI API request.
     
    start_date: The last existing date in spreadsheet + 1 (at 00:00:00)
    end_date: The previous calendar day (at 23:59:59) """
    gc = gspread.authorize(credentials)
    spreadsheet_title = "ElectricityTracker"
    spreadsheet = gc.open(spreadsheet_title)
    sheet = spreadsheet.get_worksheet(6)

    current_dates = sheet.get_all_values()
    last_date = current_dates[-1][0]
    last_date = datetime.strptime(last_date, "%Y-%m-%d")
    start_date = last_date + timedelta(days=1)
    start_date = start_date.strftime("%Y-%m-%dT00:00:00Z")

    today = datetime.now()
    end_date = today + timedelta(-1)
    end_date = end_date.strftime("%Y-%m-%dT23:59:59Z")

    return start_date, end_date