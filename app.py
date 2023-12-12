import streamlit as st
import pandas as pd
from datetime import datetime

# Load existing logbook data or create an empty DataFrame
logbook_data = pd.DataFrame(columns=['Date', 'Route', 'Grade', 'Notes'])

# Function to add a climb to the logbook
def add_climb(date, route, grade, notes):
    global logbook_data
    logbook_data = logbook_data.append({'Date': date, 'Route': route, 'Grade': grade, 'Notes': notes}, ignore_index=True)

# Streamlit UI
st.title('Climbing Logbook App')

# Sidebar for adding climbs
st.sidebar.header('Add Climb')
climb_date = st.sidebar.date_input('Date', datetime.today())
climb_route = st.sidebar.text_input('Route', '')
climb_grade = st.sidebar.text_input('Grade', '')
climb_notes = st.sidebar.text_area('Notes', '')

if st.sidebar.button('Add Climb'):
    add_climb(climb_date, climb_route, climb_grade, climb_notes)
    st.sidebar.success('Climb added to logbook!')

# Display the logbook
st.header('Climbing Logbook')
st.table(logbook_data.sort_values(by='Date', ascending=False).reset_index(drop=True))
