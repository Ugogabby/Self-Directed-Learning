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
    col1.write(":blue[Admin Key: 1.1]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM rating_1"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "role_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.1) 


with st.form("admin_0"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 1.2]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM injury_1"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "role_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.11) 





with st.form("admin_1"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 1.3]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM willing_1"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "role_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.122) 



with st.form("admin_2"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 1.4]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM emotions_1"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "role_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.13) 



with st.form("admin_3"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 1.5]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM forgive_1"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "role_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.14) 



with st.form("admin_4"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 2.1]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM Literature_2"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "quote1", "resonates_word1", "meaningful1", "reasons1", "quote2", "rephrased_quote2"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.2) 


with st.form("admin_5"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 2.2]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM benefits_2"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "physical_health", "mental_health", "relationships", "spirituality"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.3)   






with st.form("admin_6"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 2.3]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM benefits_2_3"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "role_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.4) 




with st.form("admin_7"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 2.4]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM Reflecting_2"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "role_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.5) 



with st.form("admin_8"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 2.5]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM good_2"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "good1", "response1", "good2", "response2", "good3", "response3", "good4", "response4"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.6) 



with st.form("admin_9"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 2.6]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM Decide2"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "role_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.7) 




with st.form("admin_10"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 3.1]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM feeling_3"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "feeling1", "role_res1", "feeling2", "role_res2", "feeling3", "role_res3", "feeling4", "role_res4"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.8) 




with st.form("admin_11"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 3.2]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM forgive_3"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "forgive1", "forgive_res1", "forgive2", "forgive_res2", "forgive3", "forgive_res3", "forgive4", "forgive_res4", "forgive5", "forgive_res5", "forgive6", "forgive_res6", "forgive7", "forgive_res7"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.9) 




with st.form("admin_12"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 3.3]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM release_3"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "role_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.91) 




with st.form("admin_13"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 3.5]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM motivation_3"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "role_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.1111) 




with st.form("admin_14"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 3.6]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM practical_3"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "role_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.11111) 




with st.form("admin_15"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 3.7]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM my_form3"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "my_form1", "my_form_res1", "my_form2", "my_form_res2", "my_form3", "my_form_res3"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.111111) 




with st.form("admin_16"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 4.2]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM being_4"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "being", "being_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.1122) 




with st.form("admin_17"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 4.3]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM my_hurt"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "my_hurt1", "my_hurt_res1", "my_hurt2", "my_hurt_res2"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.112) 




with st.form("admin_18"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 4.6]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM empathy4"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "empathy", "res_empathy"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.11222) 


with st.form("admin_19"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 4.7]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM assessment"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "assessment1", "assessment_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.11333) 


with st.form("admin_20"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 5.1]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM role"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "role1", "role_play_res1", "role2", "role_play_res2", "role_play_res3", "role_play_res4", "role_play_res5", "role_play_res6", "role_play_res7", "role_play_res8", "role_play_res9", "role_play_res10"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.1133) 



with st.form("admin_21"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 5.2]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM compassion"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "compassion1", "compassion_res1", "compassion2", "compassion_res2"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.114) 



with st.form("admin_22"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 5.3]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM daily_life"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "daily_life1", "daily_life1_res", "daily_life2", "daily_life2_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.1144) 



with st.form("admin_23"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 5.4]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM emotions5"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions_text", "role_resst_emotions"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.11444) 



with st.form("admin_24"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 5.5]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM forgiveness5"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "role_res_forgive1", "role_res_forgive2", "role_res_forgive3"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.115) 





with st.form("admin_25"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 5.6]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM assessments5"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions_text", "assessments_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.1154) 




with st.form("admin_26"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 6.1]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM useful_6"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "useful_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.1151) 




with st.form("admin_27"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 6.2]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM unselfish_6"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "Unselfish_res1", "Unselfish_res2"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.151) 




with st.form("admin_28"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 6.3]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM messes_6"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "messes_res1", "messes_res2"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.1511) 





with st.form("admin_29"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 6.4]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM need_forgiveness"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "need_forgiveness_res1", "need_forgiveness_res2", "need_forgiveness_res3"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.141) 





with st.form("admin_30"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 6.5]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM gratitude_6"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "gratitude_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.142) 




with st.form("admin_31"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 6.6]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM gift_6"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "gift_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.143) 




with st.form("admin_32"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 6.7]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM Question_6"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "Question_res1", "Question_res2"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.145) 




with st.form("admin_33"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 6.8]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM assessments_6"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "assessments_res_6"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.18) 




with st.form("admin_34"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 7.1]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM commit_7"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "commit_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.182) 




with st.form("admin_35"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 7.2]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM certificate_7"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "date", "forgiven_person", "reason", "forgiveness_percent", "signature"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.183) 





with st.form("admin_36"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 7.5]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM major7"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "ajor_res1", "major_res2", "major_res3", "major_res4", "major_res5", "major_res6", "major_res7", "major_res8"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.184) 





with st.form("admin_37"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 7.6]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM controlling7"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "controlling_res1", "controlling_res2", "controlling_res3", "controlling_res4", "controlling_res5"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.185) 





with st.form("admin_38"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 8.1]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM doubt_8"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "doubt_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.86) 





with st.form("admin_39"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 8.2]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM reminder8"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "Reminder_res1", "Reminder_res2"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.187) 





with st.form("admin_40"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 8.4]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM worries8"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "worries_res1", "worries_res2", "worries_res3"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.189) 





with st.form("admin_41"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 8.7]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM knowledge_ass8"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "knowledge_ass"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.188) 





with st.form("admin_42"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 9.1]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM dedicate9"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "dedicate_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=0.1189) 





with st.form("admin_43"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 9.2]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM hurts9"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "hurts_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=55) 






with st.form("admin_44"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 9.3]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM wound9"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "wound_res1", "wound_res2", "wound_res3", "wound_res4", "wound_res5", "wound_res6"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=52) 





with st.form("admin_45"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 9.4]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM heroes_9"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "heroes_res1", "heroes_res2", "heroes_res3"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=533) 





with st.form("admin_46"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 10.1]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM effort_10"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "effort_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=453) 





with st.form("admin_47"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 10.2]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM past_10"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "past_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=72) 




with st.form("admin_48"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 10.3]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM strategy_10"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "strategy_res1", "strategy_res2", "strategy_res3"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=8.11) 




with st.form("admin_49"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 10.4]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM hypothetical_10"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "hypothetical_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=9.11) 




with st.form("admin_50"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 10.5]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM everyday_10"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "everyday_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=10.11) 





with st.form("admin_51"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 10.6]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM someone_10"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "someone_res1", "someone_res2"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=11.11) 




with st.form("admin_52"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 10.7]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM campaign_10"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "campaign_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=12.11) 



with st.form("admin_53"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 10.10]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM know_10"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "know_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=13.11) 





with st.form("admin_54"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 11.5]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM evaluate_11"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "evaluate_res1", "evaluate_res2", "evaluate_res3", "evaluate_res4", "evaluate_res5", "evaluate_res6", "evaluate_res7", "evaluate_res8"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=14.11) 





with st.form("admin_56"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 12.1]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM evaluate_12"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "eval_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=15.11) 




with st.form("admin_57"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 12.3]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM decision_12"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "decision_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=16.11) 




with st.form("admin_58"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 12.4]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM again_12"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "again_res"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=17.11) 




with st.form("admin_59"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 12.6]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM time_used"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "questions", "time", "signature"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=18.11) 




with st.form("admin_60"):
    col1, col2 = st.columns([0.3, 0.7])
    col1.write(":blue[Admin Key: 12.7]")
    admin_key = col2.text_input("", value=None, placeholder="Enter Admin Key", type="password", label_visibility="collapsed")
    submitted = st.form_submit_button(":red[Submit]")

    if submitted:
       if admin_key == st.secrets["admin_key"]:
         select_query = "SELECT * FROM feedback_12"
         cursor.execute(select_query)
         all_rows = cursor.fetchall()
         conn.close()
         df = pd.DataFrame(all_rows, columns=["ID", "feedback_res1", "feedback_res2"])
         csv = convert_df(df)
       else:
          st.warning("Wrong admin key")

def message():
   return st.success("Data successfully downloded")

if csv:
   download = st.download_button(label="Download data as CSV", data=csv, file_name='collected_data.csv', mime='text/csv', on_click=message, key=19.11) 


