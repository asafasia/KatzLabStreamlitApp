import streamlit as st

page = st.sidebar.selectbox("Navigation", ["Main Page", "Chip Parameters", "Results Section"])

if page == "Main Page":
    main_page()

