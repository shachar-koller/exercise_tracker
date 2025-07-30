import streamlit as st

# Set page config
st.set_page_config(
    page_title="Exercise Tracker - Login",
    page_icon="💪",
    layout="centered"
)

def main_app():
    st.title("🏋️ Exercise Tracker Dashboard")
    
    st.divider()
    
    # Dashboard content
    st.subheader("📊 Quick Overview")
    
    # Stats cards (placeholder data)
    col1, col2, col3 = st.columns(3)
    with col1:
        #this is a placeholder. need to create a function that gets total workouts
        st.metric("Total Workouts", "12", "2")
    with col2:
        #ditto, need to get total workouts this week and last
        st.metric("This Week", "3", "1")
    with col3:
        #ditto, need to get total workouts 
        st.metric("Favorite Exercise", "Push-ups", "")
    
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