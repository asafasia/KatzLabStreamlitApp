import matplotlib.pyplot as plt
import streamlit as st
from results_utlilits import *
import pandas as pd
import plotly.express as px
from helper import project_path
from helper.save_function import ExperimentData


def results_section():
    project_dir = project_path
    st.sidebar.title("Qubit Selection")
    qubit = st.sidebar.selectbox("Choose a Qubit", options=["Qubit 1", "Qubit 2", "Qubit 3"])

    st.sidebar.title('Date Selection')
    folder = st.sidebar.selectbox('Select a Date Folder',
                                  list_folders_in_directory(
                                      f'{project_dir}/results/data'))  # Assuming data is in 'data' directory

    # Sidebar to select a file within the selected folder
    st.sidebar.title('File Selection')
    folder_path = os.path.join(f'{project_path}/results/data', folder)
    selected_file = st.sidebar.selectbox('Select a File', list_files_in_folder(folder_path))

    selected_experiment = st.selectbox("Select Experiment", options=["T1", "Power Rabi", "Power Broadening", "Ramsey", "Randomized Benchmarking", "..."])

    # # Main content for the results section
    # st.title('Graphs for Selected File')
    #
    # Load and display data from the selected file (You can replace this with your data loading logic)
    file_path = os.path.join(folder_path, selected_file)
    data = ExperimentData.load_data(file_path)
    df = pd.DataFrame.from_dict([data.experiment_properties['qubit_parameters']])

    # st.subheader(f'Contents of {selected_file}')

    st.subheader(f'{data.experiment_properties['exp_name']} exp for {data.experiment_properties['qubit']}')

    # st.subheader(f'{data.experiment_properties['exp_name']}')

    # Create an interactive line plot using Plotly Express
    import plotly.graph_objects as go

    if data.experiment_properties['exp_name'] == 'IQ Clouds':

        # df = [data.x_data, data.z_data]
        # fig = px.scatter(df)
        # st.plotly_chart(fig)

        fig = px.histogram(x=[data.x_data,data.z_data])
        st.plotly_chart(fig)

    else:
        fig = px.line(x=data.x_data, y=data.y_data, title=f'Interactive Plot for {selected_file}')
        st.plotly_chart(fig)
    # Display the DataFrame

    st.subheader('qubit parameters:')

    st.write(df.transpose())
