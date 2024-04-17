# ElectricityTracker
This is a project created for tracking household energy consumption and its cost. Through a GUI, created using Tkinter, the user is able to input their energy consumption, energy cost, and download weather data into their Google Sheets document.

## Functionalities:
- Input and upload energy consumption and cost into a Google Sheet
- Uses FMI API to download latest temperature data to compare with energy consumption
- [Google Sheets document](https://docs.google.com/spreadsheets/d/1ium8LIi9zPujZi17ntmYBx5nK3m0dsbkBwDgIDAvSHo/edit?usp=sharing) to store and visualise the data in a dashboard

![ElectricityTracker demo GIF](https://raw.githubusercontent.com/vltnnx/Electricity-Tracker/main/static/img/git-demo.gif)

## Notes for users:
Feel free to fork the project and use for yourself. Below are some helpful notes.

#### 1. Google Cloud Service Account
To update your spreadsheet using this program, you need to have a project, a service account, and a key. You can find some helpful tips into setting everything up in [this Medium article](https://medium.com/analytics-vidhya/how-to-read-and-write-data-to-google-spreadsheet-using-python-ebf54d51a72c), or in [this Python quickstart for Google Sheets API](https://developers.google.com/sheets/api/quickstart/python).

#### 2. Reading and writing into Google Sheets document
In this program, the functions read the worksheets based on their index number. So, if you create your own spreadsheet or change the order of the worksheets, be sure to make the appropriate changes to the index references in the functions

#### 3. Requesting temperature data
Downloading temperature data works by a function reading the last existing date in the users document and creating start and end dates (start = last existing date + 1, end = today - 1). A function then requests daily average temperatures from FMI's Open Data API based on those dates. 

I haven't tested how many years of temperature data could be requested, but you can add a date to the worksheet after which you want to get the data from (e.g. you want data from February 1, 2024, add the date January 31, 2024 in the spreadsheet).

#### 4. Hidden worksheets
There are multiple worksheets that are hidden, functioning to create tables for the visualisations in the dashboard. Users can modify and add new tables, visualisations, and worksheets as they wish (just remember the tip no. 2).
