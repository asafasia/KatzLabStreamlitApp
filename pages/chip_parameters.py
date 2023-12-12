import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


qubit_number = 5
T1 = [50, 60, 70, 80, 90]
T2 = [30, 40, 50, 60, 70]

single_gate_fideliltiy = [0.99, 0.98, 0.97, 0.96, 0.95]
two_qubit_gate_fidelity = [0.99, 0.98, 0.97, 0.96]

st.sidebar.title('Parameters')

# fig = px.bar_polar(T1, r="frequency", theta="direction", color="strength", template="plotly_dark",
#                    color_discrete_sequence=px.colors.sequential.Plasma_r)
#
# fig = px.bar_polar(r=T1, theta=np.array([1, 2, 3, 4, 5]) * 360, template="plotly_dark",
#                    color_discrete_sequence=px.colors.sequential.Plasma_r)
# st.plotly_chart(fig)
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Streamlit app
st.title("Quantum Computing Plot")

# Display the Matplotlib plot
st.pyplot(plt.plot(x, y))
