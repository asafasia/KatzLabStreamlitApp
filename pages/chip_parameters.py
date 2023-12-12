import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from utils.a import b

qubit_number = 5
T1 = [50, 60, 70, 80, 90]
T2 = [30, 40, 50, 60, 70]

single_gate_fideliltiy = [0.99, 0.98, 0.97, 0.96, 0.95]
two_qubit_gate_fidelity = [0.99, 0.98, 0.97, 0.96]

st.sidebar.title('Parameters')


x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)


# fig = plt.figure()

# plt.plot(x,y)

# with st.sidebar:
#     st.write("Check color")
# st.plotly_chart(fig)
