import streamlit as st
from config import connect_to_db

st.set_page_config(
    page_title="Developing Moral Resilience through Forgiveness",
    page_icon="random",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={'About': "Learn to be More Forgiving in Less Than Two Hours!"})

try:
   conn, cursor = connect_to_db()
except:
   st.write("failed to connect to the database")  

with st.form("rating_1"):
    col1, col2 = st.columns(2)
    col1.write("How forgiving are you as a person, from 0 (not at all) to 10 (completely)?")
    role_res = col2.radio('Pick one:', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=None, horizontal=True, key=1.1)
    submitted = st.form_submit_button("Submit")

    if submitted:
        if role_res is None:
            st.warning("Please select your forgiveness rating before submitting.")
        else:
            cursor.execute("""CREATE TABLE IF NOT EXISTS rating_1 ( id INTEGER PRIMARY KEY AUTOINCREMENT, role_res INTEGER)""")
            insert_query = "INSERT INTO rating_1 (role_res) VALUES (?)"
            data_to_insert = (role_res,)  # Add a comma after role_res to make it a tuple
            cursor.execute(insert_query, data_to_insert)
            conn.commit()  # Commit changes before closing connection
            conn.close()
            st.success("Data saved successfully!")



