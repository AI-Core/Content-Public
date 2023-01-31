from clean_data import clean_data
from process_data import process_data


def clean_and_process_data(data):
    # clean and process the data
    data = clean_data(data)
    data = process_data(data)

    return data
