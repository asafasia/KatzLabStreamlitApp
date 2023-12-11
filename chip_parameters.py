import streamlit as st
# import plotly.express as px
import numpy as np

def chip_parameters():
    qubit_number = 5
    T1 = [50, 60, 70, 80, 90]
    T2 = [30, 40, 50, 60, 70]

    single_gate_fideliltiy = [0.99, 0.98, 0.97, 0.96, 0.95]
    two_qubit_gate_fidelity = [0.99, 0.98, 0.97, 0.96]

    st.sidebar.title('Parameters')
    
    fig = px.bar_polar(T1, r="frequency", theta="direction", color="strength", template="plotly_dark",
                       color_discrete_sequence=px.colors.sequential.Plasma_r)

    fig = px.bar_polar(r=T1, theta=np.array([1, 2, 3, 4, 5]) * 360, template="plotly_dark",
                       color_discrete_sequence=px.colors.sequential.Plasma_r)
    st.plotly_chart(fig)
