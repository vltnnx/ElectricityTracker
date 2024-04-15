import xml.etree.ElementTree as ET
import pandas as pd

def create_df(xml_data):
    parsed_xml = ET.fromstring(xml_data.content)
    rows = []

    for member in parsed_xml.findall('.//wfs:member', namespaces={'wfs': 'http://www.opengis.net/wfs/2.0'}):
        row = []
        
        time = member.find('.//BsWfs:Time', namespaces={'BsWfs': 'http://xml.fmi.fi/schema/wfs/2.0'}).text
        time = time[:10]
        row.append(time)

        parameter_value = member.find('.//BsWfs:ParameterValue', namespaces={'BsWfs': 'http://xml.fmi.fi/schema/wfs/2.0'}).text
        row.append(parameter_value)

        rows.append(row)

    # New temperatures into a DataFrame
    new_temperatures = pd.DataFrame(data=rows, columns=["date", "temperature"])

    # Load existing temperature data
    old_temperatures = pd.read_csv("data/loaded_data.csv")

    # Append new data to existing data and create .csv
    loaded_data = pd.concat([old_temperatures, new_temperatures], ignore_index=True)
    loaded_data.to_csv("data/loaded_data.csv", index=False)

    return new_temperatures
