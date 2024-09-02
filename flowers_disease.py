import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Create a connection object.

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(
    spreadsheet = 'https://docs.google.com/spreadsheets/d/1vnKgg38X1Q3sZGwc1sRdizG61IF9zOfb/edit?usp=sharing&ouid=112800795579393298100&rtpof=true&sd=true',
    worksheet = '1012481484',
    ttl=0
)

st.dataframe(data)
