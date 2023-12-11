import streamlit as st
from streamlit import session_state


def main_page():
    # Create a primary button

    st.title("Welcome to Nadav's Lab")
    st.write("We operate a state-of-the-art 5-qubit chip.")
    st.write("This app is designed to showcase the properties and results of experiments conducted on this chip")
    st.write("To access the results section, please use the sidebar.")

