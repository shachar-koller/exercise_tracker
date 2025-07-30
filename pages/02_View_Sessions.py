import streamlit as st
import pandas as pd
import os
import json

st.set_page_config(
    page_title="Exercise Tracker - View Sessions",
    page_icon="📈",
    layout="centered"
)

def main_app():
    st.title("📈 View Sessions")
    
    st.divider()
    
    csv_file = "data.csv"
    if not os.path.exists(csv_file):
        st.warning("No sessions found. Start logging workouts first!")
        if st.button("🏋️ Log New Session"):
            st.switch_page("pages/01_Log_Session.py")
        return
    
    try:
        df = pd.read_csv(csv_file)
        
        if df.empty:
            st.info("No sessions recorded yet.")
        else:
            st.subheader(f"📊 Total Sessions: {len(df)}")
            
            for index, row in df.iterrows():
                with st.expander(f"Session: {row['name']} ({row['exercise_counter']} exercises)"):
                    if pd.notna(row['notes']) and row['notes']:
                        st.write(f"**Notes:** {row['notes']}")
                    
                    try:
                        exercises = json.loads(row['exercises'])
                        for exercise in exercises:
                            sets_display = []
                            for i, set_data in enumerate(exercise['sets'], 1):
                                if set_data['weight'] == 0.0:
                                    sets_display.append(f"{set_data['reps']}")
                                else:
                                    sets_display.append(f"{set_data['weight']} lbs x {set_data['reps']}")
                            
                            st.write(f"**{exercise['name']}:** {' | '.join(sets_display)}")
                    except (json.JSONDecodeError, KeyError):
                        st.write("Error displaying exercise data")
    
    except Exception as e:
        st.error(f"Error reading sessions: {e}")
    
    st.divider()
    
    if st.button("🏠 Return Home", use_container_width=True):
        st.switch_page("app.py")

main_app()