import streamlit as st
import pandas as pd
from config import connect_to_db

st.write('### Developing Moral Resilience through Forgiveness')
st.write("##### :blue[Welcome to the admin page, enter your admin key below to download the data]")

try:
   conn, cursor = connect_to_db()
except:
   st.write("failed to connect to the database")

def convert_df(df):
    return df.to_csv().encode('utf-8')

csv = None
with st.form("admin"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key:]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM rating_1"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "role_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message)    