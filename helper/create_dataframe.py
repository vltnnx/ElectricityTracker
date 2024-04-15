import xml.etree.ElementTree as ET
import pandas as pd

def create_df(xml_data):
    """ Parses the XML data from FMI API query into a pandas DataFrame. 
    Returns new_temperatures DataFrame. """
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

    return new_temperatures
