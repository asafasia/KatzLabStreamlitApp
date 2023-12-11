import os
import re
import pickle
import sys




def give_existing_dates(folder_path='results/data'):
    folder_path = f"{project_dir}/{folder_path}"

    dates_list = []

    # Regular expression pattern to match dates in the folder names (assuming the format YYYY-MM-DD)
    date_pattern = r'\d{2}_\d{2}_\d{4}'

    # Loop through the contents of the folder
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path) and re.match(date_pattern, item):
            dates_list.append(item)

    # Print the list of dates
    return dates_list


def list_folders_in_directory(directory):
    folders = [f.name for f in os.scandir(directory) if f.is_dir()]
    return folders


def list_files_in_folder(folder_path):
    files = os.listdir(folder_path)
    return files


def load_data(file_path):
    with open(file_path, 'rb') as file:
        loaded_data = pickle.load(file)
    return loaded_data
