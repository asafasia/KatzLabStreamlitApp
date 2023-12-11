import streamlit as st
from main_page import main_page


page = st.sidebar.selectbox("Navigation", ["Main Page", "Chip Parameters", "Results Section"])

if page == "Main Page":
    main_page()

