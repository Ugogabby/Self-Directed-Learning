<<<<<<< HEAD
import sqlite3

def connect_to_db():
  conn = sqlite3.connect("participant_data.db") 
  cursor = conn.cursor()
  return conn, cursor
