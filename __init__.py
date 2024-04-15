from helper.get_temperature import get_temperatures

temperatures = get_temperatures()

print(temperatures)
print()

import pandas as pd

df = pd.read_csv("data/loaded_data.csv")
print(df)
print()