import pandas as pd
import matplotlib.pyplot as plt
from src.utils import process_data

# Load the dataset
DATA_FILE = "data/clickstream_data.csv"

def main():
    try:
        # Read data
        data = pd.read_csv(DATA_FILE)

        # Process data
        processed_data = process_data(data)

        # Extract insights
        unique_users = processed_data['user_id'].nunique()
        most_visited_page = processed_data['page'].mode()[0]
        peak_traffic_time = processed_data['hour'].value_counts().idxmax()

        print(f"Unique Users: {unique_users}")
        print(f"Most Visited Page: {most_visited_page}")
        print(f"Peak Traffic Time: {peak_traffic_time}")

        # Visualize Traffic Patterns
        traffic_by_hour = processed_data['hour'].value_counts().sort_index()
        plt.bar(traffic_by_hour.index, traffic_by_hour.values)
        plt.xlabel("Hour")
        plt.ylabel("Traffic")
        plt.title("Websites traffic by Hour")
        plt.show()

    except FileNotFoundError:
        print(f"Error: File '{DATA_FILE}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
