import os
import pandas as pd

def load_all_stations(data_path):
    all_data = []

    for file in os.listdir(data_path):
        if file.endswith(".csv"):
            file_path = os.path.join(data_path, file)
            df = pd.read_csv(file_path)
            df["station"] = file.replace(".csv", "")
            all_data.append(df)

    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df