import streamlit as st
# from streamlit_option_menu import option_menu
from auth import login, register
from pages.Home import home_page
from pages.Recommendation import recommendation_page
from pages.About import about_page

# # Set page config
st.set_page_config(page_title="Farmers Market App", layout="centered")

# Dictionary to map page names to functions
page_dict = {
    "Home": home_page,
    "Recommendations": recommendation_page,
    "About": about_page
}

# Authentication check
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if st.session_state['logged_in']:
    # Horizontal navigation
    selected_page = option_menu(
        menu_title=None,
        options=list(page_dict.keys()),
        icons=["house", "search", "info-circle"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {"font-size": "15px", "text-align": "center", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "blue","font-size": "10px"},
        }
    )
    
    page_dict[selected_page]()
    
    # Button for logging out
    if st.button("Logout"):
        st.session_state['logged_in'] = False
        st.experimental_rerun()
else:
    # If not logged in, show login or register page
    st.title("Welcome to Farmers market recommendation system")
    auth_choice = st.radio( "",["Login", "Register"])
    if auth_choice == "Login":
        login()
    elif auth_choice == "Register":
        register()
