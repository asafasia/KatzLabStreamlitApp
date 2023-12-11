import streamlit as st
import matplotlib.pyplot as plt
from streamlit import session_state


def main_page():
    # Create a primary button

    st.title("Welcome to Nadav's Lab")
    st.write("This is the main page of your app where you can provide explanations and instructions.")
    st.write("You can use this page to introduce users to the functionality of your app.")
    st.write("To access the results section, please use the sidebar.")
