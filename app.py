import streamlit as st

from classes.data_manager import Data_Manager
from collections import Counter

# Set page config
st.set_page_config(
    page_title="Exercise Tracker - Login",
    page_icon="💪",
    layout="centered"
)

def main_app():
    dm = Data_Manager()
    
    st.title("🏋️ Exercise Tracker Dashboard")
    
    st.divider()
    
    # Dashboard content
    st.subheader("📊 Quick Overview")
    
    this_week_count, last_week_count = dm.get_weekly_workout_stats()
    more = this_week_count-last_week_count
    # Stats cards (placeholder data)
    col1, col2, col3 = st.columns(3)
    with col1:
        #this is a placeholder. need to create a function that gets total workouts
        total_workouts = dm.get_num_sessions()
        st.metric("Total Workouts", total_workouts, this_week_count)
    with col2:
        #ditto, need to get total workouts this week and last
        st.metric("This Week", this_week_count, more)
    with col3:
        all_exs = dm.get_all_exs()
        fav = ""
        if all_exs:
            fav = Counter(all_exs).most_common(1)[0][0]
        st.metric("Favorite Exercise", fav, "")
    
    st.divider()
    
    # Quick actions
    st.subheader("🚀 Quick Actions")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🏋️ Start New Workout", use_container_width=True):
            st.switch_page("pages/01_Log_Session.py")
    
    with col2:
        if st.button("📈 View Progress", use_container_width=True):
            st.switch_page("pages/02_View_Sessions.py")
    
    st.divider()


main_app()