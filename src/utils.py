import pandas as pd

def process_data(data):
    """
    - Converts timestamps to datetime objects.
    - Extracts the hour from timestamps.
    """

    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data['hour'] = data['timestamp'].dt.hour

    return data