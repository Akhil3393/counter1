import streamlit as st
import sqlite3

# Connect to the database
conn = sqlite3.connect('app_database.db')
cursor = conn.cursor()

# Initialize the counter if not exists
cursor.execute('CREATE TABLE IF NOT EXISTS purchase_counter (count INT);')
cursor.execute('INSERT OR IGNORE INTO purchase_counter VALUES (0);')

# Display the current count on the Streamlit app
current_count = cursor.execute('SELECT count FROM purchase_counter;').fetchone()[0]
count_display = st.empty()  # Placeholder for live update

# Display the current count
count_display.text(f'Current count: {current_count}')

# Simulate a purchase event
# This would be triggered in your app when a user makes a purchase
# For example, after a successful payment
purchase_event = st.button("Simulate Purchase")

if purchase_event:
    # Increment the counter in the database
    cursor.execute('UPDATE purchase_counter SET count = count + 1;')
    conn.commit()

    # Update the live display with the new count
    current_count = cursor.execute('SELECT count FROM purchase_counter;').fetchone()[0]
    count_display.text(f'Count incremented! New count: {current_count}')

# Close the database connection
conn.close()
