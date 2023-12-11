import streamlit as st
from main_page import main_page
# from chip_parameters import chip_parameters


page = st.sidebar.selectbox("Navigation", ["Main Page", "Chip Parameters", "Results Section"])

if page == "Main Page":
    main_page()

# elif page == "Chip Parameters":
#     chip_parameters()



x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Streamlit app
st.title("Quantum Computing Plot")

# Display the Matplotlib plot
st.pyplot(plt.plot(x, y))
