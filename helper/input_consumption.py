from tkinter import messagebox
import gspread
from google.oauth2.service_account import Credentials
from config import credentials_file

class ElectricityTracker:
    """ Takes the input data from root_input window and adds
    the data into the spreadsheet. """
    def __init__(self, start_day, end_day, kwh, cost_consumption, cost_transfer):
        self.start_day = start_day
        self.end_day = end_day
        self.kwh = kwh
        self.cost_consumption = cost_consumption
        self.cost_transfer = cost_transfer

        self.credentials_file = credentials_file
        self.credentials = Credentials.from_service_account_file(self.credentials_file, scopes=[
        'https://spreadsheets.google.com/feeds', 
        'https://www.googleapis.com/auth/drive'
        ])
        self.gc = gspread.authorize(self.credentials)
        self.spreadsheet_title = "ElectricityTracker"
        self.spreadsheet = self.gc.open(self.spreadsheet_title)
        self.sheet = self.spreadsheet.get_worksheet(5)


    def append_to_sheet(self):
        next_row = len(self.sheet.get_all_values()) + 1
        data = [self.start_day, self.end_day, self.kwh, self.cost_consumption, self.cost_transfer]
        row_range = f"A{next_row}"
        self.sheet.update(values=[data], range_name=row_range)

        messagebox.showinfo("Success", "Consumption data added")