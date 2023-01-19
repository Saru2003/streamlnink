import streamlit as st
import pandas as pd
# my_form = st.form(key = "some")
# name = my_form.text_input(label = "Enter the model name")
# age = my_form.text_input(label = "Enter the age")
# submit = my_form.form_submit_button(label = "Submit this form")
import gspread
from oauth2client.service_account import ServiceAccountCredentials



scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("final.json", scope)
client = gspread.authorize(creds)
sheet = client.open("streamlink").sheet1


header=st.container()
dataset=st.container()
features=modelTraining=st.container()
with header:
    st.title("hello")
    inp=st.text_input('something')
    age=st.text_input('something_age')
    if st.button("click"):
        print(inp,age)
        row=[inp,age]
        data=sheet.get_all_records()
        sheet.insert_row(row,len(data)+2)
        #pprint(sheet.get_all_records)
    
