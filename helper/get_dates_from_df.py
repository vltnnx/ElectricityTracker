import pandas as pd
from datetime import datetime, timedelta

def get_dates():
    loaded_data = pd.read_csv("data/loaded_data.csv")
    last_date = loaded_data["date"].iloc[-1]
    last_date = datetime.strptime(last_date, "%Y-%m-%d")
    start_date = last_date + timedelta(days=1)
    start_date = start_date.strftime("%Y-%m-%dT00:00:00Z")

    today = datetime.now()
    end_date = today + timedelta(-1)
    end_date = end_date.strftime("%Y-%m-%dT23:59:59Z")

    return start_date, end_date


# # Test above function
# start_date, end_date = get_dates()
# print("Start date: ", start_date)
# print("End date: ", end_date)