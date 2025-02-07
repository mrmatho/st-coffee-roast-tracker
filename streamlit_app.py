import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# Function to authenticate and connect to the Google Spreadsheet
def authenticate_and_connect():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(st.secrets["GOOGLE_API_CREDENTIALS"], scope)
    client = gspread.authorize(credentials)
    sheet = client.open_by_key(st.secrets["SPREADSHEET_ID"]).sheet1
    return sheet

# Function to write input data to the Google Spreadsheet
def write_data_to_sheet(sheet, data):
    sheet.append_row(data)

# Streamlit form to input roast data
st.title("Coffee Roast Tracker")

with st.form("roast_form"):
    temperature = st.text_input("Temperature (°C) after each minute (comma-separated):")
    browning_stage = st.text_input("Time of Browning Stage (minutes):")
    first_crack = st.text_input("Time of First Crack (minutes):")
    cooled = st.text_input("Time of Cooled (minutes):")
    beans_out = st.text_input("Time of Beans Out (minutes):")
    weight_in = st.text_input("Weight In (grams):")
    weight_out = st.text_input("Weight Out (grams):")
    variety = st.text_input("Variety of Coffee Bean:")
    color = st.text_input("Color of Finished Roast:")

    submitted = st.form_submit_button("Submit")

    if submitted:
        sheet = authenticate_and_connect()
        data = [
            temperature,
            browning_stage,
            first_crack,
            cooled,
            beans_out,
            weight_in,
            weight_out,
            variety,
            color
        ]
        write_data_to_sheet(sheet, data)
        st.success("Roast data submitted successfully!")
