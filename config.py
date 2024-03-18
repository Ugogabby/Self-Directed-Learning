<<<<<<< HEAD
import sqlite3

def connect_to_db():
  conn = sqlite3.connect("participant_data.db") 
  cursor = conn.cursor()
=======
import sqlite3

def connect_to_db():
  conn = sqlite3.connect("participant_data.db") 
  cursor = conn.cursor()
>>>>>>> c07242953e66244744d7a96d07be080b640b84ab
  return conn, cursor