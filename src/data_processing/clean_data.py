import pandas as pd

def clean_data(df):
    # 1. Create datetime column
    df["datetime"] = pd.to_datetime(df[["year", "month", "day", "hour"]])
        # 2. Drop columns we no longer need
    df = df.drop(columns=["No", "year", "month", "day", "hour"])
        # 3. Handle missing values (simple method for now) fills with the previous value in the column
    df = df.fillna(method="ffill")
    return df