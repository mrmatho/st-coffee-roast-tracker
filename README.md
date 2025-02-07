# Coffee Roast Tracker

This project is a coffee roast tracker built using Streamlit. The purpose of this tracker is to help coffee roasters log and monitor the details of their coffee roasting process. The data is written out to a Google Spreadsheet, which can be publicly available for now. Each roast tracks the temperature after each minute (from 0 to 12-30), as well as the time of "Browning Stage", "First Crack", "Cooled", and "Beans Out". It also tracks the weight in and weight out, the variety of the coffee bean, and the color of the finished roast.

## Setup

### Dependencies

To set up the project, you need to install the following dependencies:

- streamlit
- gspread
- oauth2client

You can install these dependencies using the following command:

```sh
pip install -r requirements.txt
```

### Environment Variables

You need to set up the following environment variables for the project:

- `GOOGLE_API_CREDENTIALS`: Path to your Google API credentials JSON file
- `SPREADSHEET_ID`: The ID of your Google Spreadsheet

## Running the Streamlit App

To run the Streamlit app, use the following command:

```sh
streamlit run streamlit_app.py
```
