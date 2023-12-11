import streamlit as st
from main_page import main_page
from experiment_results import results_section
from chip_parameters import chip_parameters

page = st.sidebar.selectbox("Navigation", ["Main Page", "Chip Parameters", "Results Section"])

if page == "Main Page":
    main_page()
elif page == "Chip Parameters":
    chip_parameters()
elif page == "Results Section":
    results_section()
