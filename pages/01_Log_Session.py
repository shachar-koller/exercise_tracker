import streamlit as st
import sys
import os
from datetime import date
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from classes.exercise import Exercise
from classes.session import Session
from classes.data_manager import Data_Manager

st.set_page_config(
    page_title="Exercise Tracker - Log New Session",
    page_icon="💪",
    layout="centered"
)

def main_app():
    st.title("🏋️ Data Logging")

    data_manager = Data_Manager()
    
    st.divider()

    session_date = st.date_input("Session Date", value=date.today())
    
    if "current_session" not in st.session_state:
        st.session_state.current_session = Session(str(session_date))
    
    if str(session_date) != st.session_state.current_session.name:
        st.session_state.current_session = Session(str(session_date))
    
    st.subheader("📊 Insert New Exercise Below")

    with st.form("exercise_form"):
        name = st.text_input("Exercise Name")
        st.write("Enter details for your exercise:")

        sets_data = []
        for i in range(1, 5):
            col1, col2 = st.columns(2)
            with col1:
                reps = st.number_input(f"Set {i} Reps", min_value=0, step=1, key=f"reps_{i}")
            with col2:
                weight = st.number_input(f"Set {i} Weight (lb)", min_value=0.0, step=0.5, key=f"weight_{i}")
            
            if reps > 0 or weight > 0:
                sets_data.append({"weight": weight, "reps": reps})
                
        submitted = st.form_submit_button("Add Exercise")
        if submitted:
            if name and sets_data:
                exercise = Exercise(name=name, sets=sets_data)
                st.session_state.current_session.add_exercise(exercise)
                st.success(f"Exercise {name} added!")
                st.rerun()
            else:
                st.error("Please enter an exercise name and at least one set with reps or weight.")

    if hasattr(st.session_state.current_session, 'exercises') and st.session_state.current_session.exercises:
        st.subheader("Current Session Exercises:")
        for exercise in st.session_state.current_session.exercises:
            st.write(f"- {exercise.name}")

    st.divider()    
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💾 Save Session", use_container_width=True):
            data_manager.add_session(st.session_state.current_session)
            data_manager.write_sessions()
            st.success("Session saved!")
            del st.session_state.current_session
    
    with col2:
        if st.button("🏋️ Return Home", use_container_width=True):
            st.switch_page("app.py")

main_app()