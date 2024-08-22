import streamlit as st
import pandas as pd

# Load users data
def load_users():
    try:
        return pd.read_csv('data/users.csv')
    except FileNotFoundError:
        # Create an empty DataFrame if the file doesn't exist
        df = pd.DataFrame(columns=['username', 'password', 'user_type'])
        df.to_csv('data/users.csv', index=False)
        return df

def save_users(users_df):
    users_df.to_csv('data/users.csv', index=False)


def login():
    st.title("Login")
    users_df = load_users()
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username in users_df['username'].values:
            stored_password = users_df[users_df['username'] == username]['password'].values[0]
            if stored_password == password:
                st.success("Logged in successfully")
                st.session_state['logged_in'] = True
                st.experimental_rerun()  # Redirect to home page
            else:
                st.error("Incorrect password")
        else:
            st.error("Username not found")

def register():
    st.title("Register")
    users_df = load_users()
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    user_type = st.selectbox("Register as", ["User", "Farmer"])
    
    if st.button("Register"):
        if username in users_df['username'].values:
            st.error("Username already taken")
        else:
            new_user = pd.DataFrame([[username, password, user_type]], columns=['username', 'password', 'user_type'])
            users_df = pd.concat([users_df, new_user], ignore_index=True)
            save_users(users_df)
            st.success("Registered successfully. Please log in.")
            st.experimental_rerun()  # Redirect to login page
